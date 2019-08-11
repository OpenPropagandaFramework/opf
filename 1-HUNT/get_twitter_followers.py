#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ujson as json
import psycopg2
import twint

def database_connection():
	postgresconn = psycopg2.connect("dbname='prop' user='CHANGEME' password='CHANGEME' host='CHANGEME'")
	postgresconn.autocommit = True
	postgrescur = postgresconn.cursor()
	return postgrescur, postgresconn

def twint_getfollowers(user, postgrescur):
	config = twint.Config()
	config.Username = user
	config.Limit = 20000
	config.Store_object = True
	twint.run.Followers(config)
	followers_obj = twint.output.follow_object
	follower_json = json.dumps(followers_obj)
	follower_json = json.loads(follower_json)
	for follower in follower_json[user]['followers']:
		postgrescur.execute("INSERT INTO queue (username) VALUES (%s) ON CONFLICT (username) DO NOTHING;", (follower,))

def twint_getfollowing(user, postgrescur):
	config = twint.Config()
	config.Username = user
	config.Limit = 20000
	config.Store_object = True
	twint.run.Following(config)
	following_obj = twint.output.follow_object
	following_json = json.dumps(following_obj)
	following_json = json.loads(following_json)
	for following in following_json[user]['following']:
		postgrescur.execute("INSERT INTO queue (username) VALUES (%s) ON CONFLICT (username) DO NOTHING;", (following,))

def run():
    postgrescur, postgresconn = database_connection()
    postgrescur.execute("SELECT username FROM users WHERE content_score >= 25 AND primary_class = 'discredit_left' ORDER BY random();")
    user = postgrescur.fetchone()
    user = user[0]
    print(user)
    twint_getfollowers(user, postgrescur)
    twint_getfollowing(user, postgrescur)
    postgrescur.close()
    postgresconn.close()    

while 1==1:
	run()
