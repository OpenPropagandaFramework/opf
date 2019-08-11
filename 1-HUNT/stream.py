#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tweepy
import json
import psycopg2

consumer_key="CHANGEME"
consumer_secret="CHANGEME"
access_token="CHANGEME"
access_token_secret="CHANGEME"

def database_connection():
	postgresconn = psycopg2.connect("dbname='prop' user='CHANGEME' password='CHANGEME' host='CHANGEME'")
	postgresconn.autocommit = True
	postgrescur = postgresconn.cursor()
	return postgrescur, postgresconn

def get_stream_hashes():
	postgrescur, postgresconn = database_connection()
	postgrescur.execute("SELECT ioc_hashtag FROM ioc_hashtags;")
	all_hashtags = postgrescur.fetchall()
	all_list = []
	for hashtag in all_hashtags:
		all_list.append(hashtag[0])
	postgrescur.close()
	postgresconn.close()
	return all_list

class MyStreamListener(tweepy.StreamListener):
	def on_error(self, status_code):
		print('Error: ' + repr(status_code))
		return False
	def on_data(self, data):
		postgrescur, postgresconn = database_connection()
		datajson = json.loads(data)
		username = datajson['user']['screen_name']
		postgrescur.execute("INSERT INTO queue (username) VALUES (%s) ON CONFLICT (username) DO NOTHING;", (username,))
		postgrescur.close()
		postgresconn.close()

def get_twitter_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return twitter_api


def stream():
    twitter_api = get_twitter_auth()
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = twitter_api.auth, listener=myStreamListener)
    all_ioc_hashes = get_stream_hashes()
    myStream.filter(track=all_ioc_hashes)

stream()