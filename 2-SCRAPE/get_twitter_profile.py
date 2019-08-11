#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import datetime
import ujson as json
import requests
import psycopg2
import argparse
import boto3

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

def user_exists(user, postgrescur):
    postgrescur.execute("SELECT * FROM users WHERE username = %s", (user,))
    return postgrescur.fetchone() is not None

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

def scoring(user, bhashtag_count, following_per_day, likes_per_day, followers_per_day, tweets_per_day, verified):
    # Scoring for Blacklist Hashtag
    if bhashtag_count == 0:
        bhash_score = 0
    if bhashtag_count == 1:
        bhash_score = 100
    if bhashtag_count == 2:
        bhash_score = 150
    if bhashtag_count >= 3:
        bhash_score = 200
    if following_per_day <= 3:
        following_score = 0
    if following_per_day > 3 and following_per_day <= 6:
        following_score = 50
    if following_per_day > 6 and following_per_day <= 10:
        following_score = 75
    if following_per_day > 10 and following_per_day <= 20:
        following_score = 125
    if following_per_day > 20:
        following_score = 200
    if likes_per_day <= 50:
        like_score = 0
    if likes_per_day > 50 and likes_per_day <= 75:
        like_score = 100
    if likes_per_day > 75 and likes_per_day <= 120:
        like_score = 150
    if likes_per_day > 120:
        like_score = 200
    if followers_per_day <= 10:
        follower_score = 0
    if followers_per_day > 10 and followers_per_day <= 20:
        follower_score = 25
    if followers_per_day > 20 and followers_per_day <= 30:
        follower_score = 50
    if followers_per_day > 30 and followers_per_day <= 40:
        follower_score = 75
    if followers_per_day > 40:
        follower_score = 100
    if tweets_per_day <= 23:
        tweet_score = 0
    if tweets_per_day > 23 and tweets_per_day <= 32:
        tweet_score = 25
    if tweets_per_day > 32 and tweets_per_day <= 63:
        tweet_score = 50
    if tweets_per_day > 63 and tweets_per_day <= 88:
        tweet_score = 75
    if tweets_per_day > 88:
        tweet_score = 100
    if verified == True:
    	verified_score = -10000
    else:
    	verified_score = 0
    total_score = bhash_score+following_score+like_score+follower_score+tweet_score+verified_score
    return total_score, bhash_score, following_score, like_score, follower_score, tweet_score, verified_score


def get_twitter_user(twitter_api, twitter_user, postgrescur, postgresconn):
    postgrescur.execute("SELECT ioc_hashtag, ioc_classification FROM ioc_hashtags;")
    blacklist_hashtags = postgrescur.fetchall()
    now = datetime.datetime.now()
    try:
        user_info = twitter_api.get_user(screen_name=twitter_user)
        protected = user_info.protected
        if protected == True:
            postgrescur.execute("UPDATE users SET status = 'private' WHERE username = %s", (twitter_user,))
        else:
            postgrescur.execute("UPDATE users SET status = 'active' WHERE username = %s", (twitter_user,))
        twitter_id = json.dumps(user_info.name)
        description = json.dumps(user_info.description)
        geo_enabled = user_info.geo_enabled
        verified = user_info.verified
        if verified == 'False':
        	verified = False
        if verified == 'True':
        	verified = True
        created_date = user_info.created_at
        followers = user_info.followers_count
        num_of_tweets = user_info.statuses_count
        extended_profile = user_info.has_extended_profile
        following = user_info.friends_count
        total_likes = user_info.favourites_count
        if user_info.url == None:
            url = False
            full_url = 'None'
        else:
            url = True
            full_url = 'None'
            # try:
            #     full_url = requests.get(user_info.url, verify=False, timeout=1).url
            # except:
            #     print("Requests Error")
            #     full_url = 'None'
        days_since_joining = (now - created_date).days
        tweets_per_day = float(num_of_tweets) / float(days_since_joining)
        likes_per_day = float(total_likes) / float(days_since_joining)
        following_per_day = float(following) / float(days_since_joining)
        followers_per_day = float(followers) / float(days_since_joining)
        if '\\u' in twitter_id:
            emoji_name = True
        else:
            emoji_name = False
        if '\\u' in description:
            emoji_description = True
        else:
            emoji_description = False
        if '#' in description:
            hashtag_description = True
        else:
            hashtag_description = False
        if emoji_name == True and emoji_description == True:
            emoji_double = True
        else:
            emoji_double = False
        if emoji_name == True and emoji_description == True and hashtag_description == True:
            emoji_triple = True
        else:
            emoji_triple = False
        if geo_enabled == True and extended_profile == True:
            geo_extended = True
        else:
            geo_extended = False
        bhashtag_count = 0
        for bhashtag in blacklist_hashtags:
            if bhashtag[0] in description:
                bhashtag_count+=1
            else:
                pass
        total_score, bhash_score, following_score, like_score, follower_score, tweet_score, verified_score = scoring(twitter_user, bhashtag_count, following_per_day, likes_per_day, followers_per_day, tweets_per_day, verified)
        postgrescur.execute("INSERT INTO users (username, followers, followers_per_day, following, following_per_day, days_since_joining, num_of_tweets, tweets_per_day, likes, likes_per_day, hashtag_desc, emoji_name, emoji_double, emojihash_triple, geo_extended, bhash_count, has_profile_url, profile_url, account_score, account_score_bhash, account_score_tweets, account_score_following, account_score_follower, account_score_likes, verified) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (username) DO NOTHING;", (twitter_user, followers, following_per_day, following, following_per_day, days_since_joining, num_of_tweets, tweets_per_day, total_likes, likes_per_day, hashtag_description, emoji_name, emoji_double, emoji_triple, geo_extended, bhashtag_count, url, full_url, total_score, bhash_score, tweet_score, following_score, follower_score, like_score, verified))
    except tweepy.TweepError as err:
        if err.api_code == 63:
            postgrescur.execute("UPDATE users SET status = 'suspended' WHERE username = %s", (twitter_user,))
            return
        if err.api_code == 50: 
            postgrescur.execute("UPDATE users SET status = 'deleted' WHERE username = %s", (twitter_user,))    
    return

def run():
    twitter_api = get_twitter_auth()
    postgrescur, postgresconn = database_connection()
    postgrescur.execute("SELECT username FROM queue TABLESAMPLE BERNOULLI(1) LIMIT 1;")
    user = postgrescur.fetchone()
    user = user[0]
    user_exists_bool = user_exists(user, postgrescur)
    if user_exists_bool == True:
    	postgrescur.execute("DELETE FROM queue WHERE username = %s;", (user,))
    	postgrescur.close()
    	postgresconn.close()    
    	return
    try:
        get_twitter_user(twitter_api, user, postgrescur, postgresconn)
    except Exception as e:
        print(e)
        error = str(e)
        postgrescur.execute("INSERT INTO fail_queue (username, error) VALUES (%s, %s) ON CONFLICT (username) DO NOTHING;", (user,error))
    postgrescur.execute("DELETE FROM queue WHERE username = %s;", (user,))
    postgrescur.close()
    postgresconn.close()    


while 1==1:
	run()
