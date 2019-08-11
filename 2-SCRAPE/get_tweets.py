#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import datetime
import ujson as json
import tldextract
import psycopg2
import emoji
import argparse
import requests
import boto3

#########
#
# Edit the variables below in order to get the script working. The Twitter Developer API allows anyone to generate the four keys below - you need all four for authentication against the API to work.
#
#########
consumer_keys = ['CHANGEME', 'CHANGEME']
consumer_secrets = ['CHANGEME', 'CHANGEME']
access_tokens = ['CHANGEME', 'CHANGEME']
access_token_secrets = ['CHANGEME', 'CHANGEME']
aws_region = 'CHANGEME'

parser = argparse.ArgumentParser(description='This script gets tweets for users defined by the SQL query specified.')
parser.add_argument('--credtype', type=str, default='local', help='Set the credential type here. You can leave this at the default "local" if running the script on non-AWS infrastructure. The option "aws" will grab the credential placement number from AWS tags - which is useful for running this tool at large scales.')
parser.add_argument('--creds', type=int, default=0, help='Specify the API credentials to use, based on the position in the Python list. Edit this script and add your Twitter API creds, this flag defaults to using the first credential set.')
args = parser.parse_args()

def database_connection():
    postgresconn = psycopg2.connect("dbname='CHANGEME' user='CHANGEME' password='CHANGEME' host='CHANGEME'")
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

def parse_tweet_text(text, user, now, postgrescur, tweet_id):
    text = text.replace("\n", " ")
    text = emoji.get_emoji_regexp().sub(u'', text)
    all_words = text.split(" ")
    for word in all_words:
        if '#' in word:
            word = word.replace("…", "").rstrip()
            postgrescur.execute("INSERT INTO hashtags (hashtag_user, hashtag, timestamp, tweet_id) VALUES (%s, %s, %s, %s) ON CONFLICT (tweet_id) DO NOTHING;", (user, word, now, tweet_id))

def get_tweets(twitter_api, user, postgrescur):
    postgrescur.execute("SELECT ioc_hashtag FROM ioc_hashtags;")
    blacklist_hashtags = postgrescur.fetchall()
    now = datetime.datetime.now()
    all_tweets = tweepy.Cursor(twitter_api.user_timeline, screen_name=user, tweet_mode='extended').items(100)
    has_place = False
    has_limited_place = False
    i=0
    for status in all_tweets:
        status_json = json.dumps(status._json)
        status_json = json.loads(status_json)
        tweet_id = status_json['id_str']
        device = status_json['source']
        if 'iPhone' in device:
            device = 'Twitter for iPhone'
        if 'Android' in device:
            device = 'Twitter for Android'
        if 'Twitter Web App' in device:
            device = 'Twitter Mobile Website'
        if 'Twitter Web Client' in device:
            device = 'Twitter Desktop Website'
        #lang = status_json['lang']
        created_at = status.created_at
        place = status_json['place']
        if place != None and has_place == False:
            if status_json['place']['place_type'] == 'city':
                geo_name = status_json['place']['full_name']
                geo_name = geo_name.split(',')
                geo_city = geo_name[0].rstrip()
                geo_state = geo_name[1]
                geo_country = status_json['place']['country']
                has_place = True
                postgrescur.execute("UPDATE users SET geo_city = %s, geo_state = %s, geo_country = %s WHERE username = %s;", (geo_city, geo_state, geo_country, user))
            else:
                geo_city = 'None'
                geo_state = status_json['place']['name']
                geo_country = status_json['place']['country']
                has_limited_place = True
                postgrescur.execute("UPDATE users SET geo_city = %s, geo_state = %s, geo_country = %s WHERE username = %s;", (geo_city, geo_state, geo_country, user))
        if i == 99 and (has_place == False and has_limited_place == False):
            postgrescur.execute("UPDATE users SET geo_city = 'None', geo_state = 'None', geo_country = 'None' WHERE username = %s;", (user,))
        i+=1
        try:
            url = status_json['entities']['urls'][0]['expanded_url']
        except:
            url = 'None'
        try:
            retweet = True
            text = status_json['retweeted_status']['full_text']
            parse_tweet_text(text, user, now, postgrescur, tweet_id)
            original_tweet_user = status_json['retweeted_status']['user']['screen_name']
            original_user_following = status_json['retweeted_status']['user']['friends_count']
            original_favourites_count = status_json['retweeted_status']['user']['favourites_count']
            original_description = status_json['retweeted_status']['user']['description']
            original_followers_count = status_json['retweeted_status']['user']['followers_count']
            verified = status_json['retweeted_status']['user']['verified']
            num_of_tweets = status_json['retweeted_status']['user']['statuses_count']
            if verified == 'True':
            	verified = True
            if verified == 'False':
            	verified = False
            days_since_joining = (now - status.retweeted_status.user.created_at).days
            likes_per_day = float(original_favourites_count) / float(days_since_joining)
            following_per_day = float(original_user_following) / float(days_since_joining)
            followers_per_day = float(original_followers_count) / float(days_since_joining)
            tweets_per_day = float(num_of_tweets) / float(days_since_joining)
            bhashtag_count = 0
            for bhashtag in blacklist_hashtags:
                if bhashtag[0] in original_description:
                    bhashtag_count+=1
                else:
                    pass
            total_score, bhash_score, following_score, like_score, follower_score, tweet_score, verified_score = scoring(user, bhashtag_count, following_per_day, likes_per_day, followers_per_day, tweets_per_day, verified)
            postgrescur.execute("INSERT INTO retweeted_users (retweeted_user, timestamp, score, tweet_id, username) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (tweet_id) DO NOTHING;", (original_tweet_user, now, total_score, tweet_id, user))
            try:
                original_url = status_json['retweeted_status']['entities']['urls'][0]['expanded_url']
            except:
                original_url = 'None'
        except Exception as e:
            retweet = False
            text = status_json['full_text']
            parse_tweet_text(text, user, now, postgrescur, tweet_id)
            original_tweet_user = 'None'
            original_url = 'None'
            total_score = 0
        if url != 'None':
            extract = tldextract.extract(url)
            domain = extract.registered_domain
            postgrescur.execute("INSERT INTO links (link_user, link_url, link_domain, timestamp, tweet_id) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (tweet_id) DO NOTHING;", (user, url, domain, now, tweet_id))
        if original_url != 'None':
            extract = tldextract.extract(original_url)
            domain = extract.registered_domain
            postgrescur.execute("INSERT INTO links (link_user, link_url, link_domain, timestamp, tweet_id) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (tweet_id) DO NOTHING;", (user, original_url, domain, now, tweet_id))

def run():
    now = datetime.datetime.now()
    twitter_api = get_twitter_auth()
    postgrescur, postgresconn = database_connection()
    postgrescur.execute("SELECT username FROM users TABLESAMPLE BERNOULLI(1) WHERE content_score >= 100 LIMIT 1;")
    user = postgrescur.fetchone()
    user = user[0]
    print(user)
    try:
        get_tweets(twitter_api, user, postgrescur)
    except Exception as e:
    	print(e)
    	error = str(e)
    	postgrescur.execute("INSERT INTO fail_queue (username, error) VALUES (%s, %s) ON CONFLICT (username) DO NOTHING;", (user,error))
    postgrescur.execute("UPDATE users SET last_scrape = %s WHERE username = %s;", (now, user))
    postgrescur.close()
    postgresconn.close()    

while 1==1:
	run()
