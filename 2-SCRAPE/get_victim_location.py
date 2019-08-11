#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import datetime
import ujson as json
import tldextract
import psycopg2
import emoji
import argparse

parser = argparse.ArgumentParser(description='Gets Tweets')
parser.add_argument('creds', type=int, help='Creds To Use')
args = parser.parse_args()

def database_connection():
    postgresconn = psycopg2.connect("dbname='CHANGEME' user='CHANGEME' password='CHANGEME' host='CHANGEME'")
    postgresconn.autocommit = True
    postgrescur = postgresconn.cursor()
    return postgrescur, postgresconn

def get_twitter_auth():
    key = args.creds
    consumer_keys = ['CHANGEME']
    consumer_secrets = ['CHANGEME']
    access_tokens = ['CHANGEME']
    access_token_secrets = ['CHANGEME']
    consumer_key = consumer_keys[key]
    consumer_secret = consumer_secrets[key]
    access_token = access_tokens[key]
    access_token_secret = access_token_secrets[key]	
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return twitter_api

def get_tweets(twitter_api, user, postgrescur, primary_class):
    postgrescur.execute("SELECT ioc_hashtag, ioc_classification FROM ioc_hashtags;")
    blacklist_hashtags = postgrescur.fetchall()
    now = datetime.datetime.now()
    all_tweets = tweepy.Cursor(twitter_api.user_timeline, screen_name=user, tweet_mode='extended').items(200)
    has_place = False
    has_limited_place = False
    i=0
    for status in all_tweets:
        status_json = json.dumps(status._json)
        status_json = json.loads(status_json)
        tweet_id = status_json['id_str']
        place = status_json['place']
        if place != None and has_place == False:
            if status_json['place']['place_type'] == 'city':
                geo_name = status_json['place']['full_name']
                geo_name = geo_name.split(',')
                geo_city = geo_name[0]
                geo_state = geo_name[1]
                geo_country = status_json['place']['place_type']
                has_place = True
                print(user, geo_city, geo_state, geo_country, primary_class)
            else:
                geo_city = 'None'
                geo_state = status_json['place']['name']
                geo_country = status_json['place']['place_type']
                has_limited_place = True
                print(user, geo_city, geo_state, geo_country, primary_class)
        if i == 199 and (has_place == False and has_limited_place == False):
            print(user, "No Location")
        i+=1
        # postgrescur.execute("INSERT INTO retweeted_users (retweeted_user, timestamp, score, tweet_id) VALUES (%s, %s, %s, %s) ON CONFLICT (tweet_id) DO NOTHING;", (user, now, total_score, tweet_id))
        # postgrescur.execute("INSERT INTO links (link_user, link_url, link_domain, timestamp, tweet_id) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (tweet_id) DO NOTHING;", (user, original_url, domain, now, tweet_id))

def run():
    now = datetime.datetime.now()
    twitter_api = get_twitter_auth()
    postgrescur, postgresconn = database_connection()
    postgrescur.execute("SELECT username,primary_class FROM users WHERE (primary_class = 'potential_victim' OR content_score < ) AND status = 'active' ORDER BY random();")
    user = postgrescur.fetchone()
    primary_class = user[1]
    user = user[0]
    get_tweets(twitter_api, user, postgrescur, primary_class)
    postgrescur.close()
    postgresconn.close()    

while 1==1:
	run()
