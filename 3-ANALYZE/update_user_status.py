#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import datetime
import ujson as json
import requests
import psycopg2
import requests
import boto3
import argparse

#########
#
# Edit the variables below in order to get the script working. The Twitter Developer API allows anyone to generate the four keys below - you need all four for authentication against the API to work.
#
#########
consumer_keys = ['CHANGEME']
consumer_secrets = ['CHANGEME']
access_tokens = ['CHANGEME']
access_token_secrets = ['CHANGEME']
aws_region = 'CHANGEME'

parser = argparse.ArgumentParser(description='This script gets tweets for users defined by the SQL query specified.')
parser.add_argument('--credtype', type=str, default='local', help='Set the credential type here. You can leave this at the default "local" if running the script on non-AWS infrastructure. The option "aws" will grab the credential placement number from AWS tags - which is useful for running this tool at large scales.')
parser.add_argument('--creds', type=int, default=0, help='Specify the API credentials to use, based on the position in the Python list. Edit this script and add your Twitter API creds, this flag defaults to using the first credential set.')
args = parser.parse_args()


def database_connection():
    postgresconn = psycopg2.connect("dbname='prop' user='CHANGEME' password='CHANGEME' host='CHANGEME'")
    postgresconn.autocommit = True
    postgrescur = postgresconn.cursor()
    return postgrescur, postgresconn

def get_twitter_auth():
    if args.credtype == 'aws':
        r = requests.get("http://169.254.169.254/latest/dynamic/instance-identity/document")
        response_json = r.json()
        region = response_json.get('region')
        instance_id = response_json.get('instanceId')
        ec2 = boto3.resource('ec2', region_name=region)
        instance = ec2.Instance(instance_id)
        tag = instance.tags
        for one_tag in tag:
            if one_tag.get('Key') == 'creds':
                key = one_tag.get('Value')
                key = int(key)        
    else:
        key = args.creds
    consumer_key = consumer_keys[key]
    consumer_secret = consumer_secrets[key]
    access_token = access_tokens[key]
    access_token_secret = access_token_secrets[key] 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return twitter_api

def update_twitter_user(twitter_api, twitter_user, postgrescur, postgresconn):
    try:
        user_info = twitter_api.get_user(screen_name=twitter_user)
        protected = user_info.protected
        if protected == True:
            postgrescur.execute("UPDATE users SET status = 'private' WHERE username = %s", (twitter_user,))
            return
        else:
            postgrescur.execute("UPDATE users SET status = 'active' WHERE username = %s", (twitter_user,))
            return
    except tweepy.TweepError as err:
        if err.api_code == 63:
            postgrescur.execute("UPDATE users SET status = 'suspended' WHERE username = %s", (twitter_user,))
            return
        if err.api_code == 50: 
            postgrescur.execute("UPDATE users SET status = 'deleted' WHERE username = %s", (twitter_user,))
            return
        else:
            print(err)

def run(postgrescur, postgresconn, twitter_api):
    postgrescur.execute("SELECT username FROM users TABLESAMPLE BERNOULLI(1) WHERE status is null LIMIT 1;")
    all_users = postgrescur.fetchone()
    user = all_users[0]
    update_twitter_user(twitter_api, user, postgrescur, postgresconn)

postgrescur, postgresconn = database_connection()
twitter_api = get_twitter_auth()
while 1==1:
    run(postgrescur, postgresconn, twitter_api)

postgrescur.close()
postgresconn.close()    

