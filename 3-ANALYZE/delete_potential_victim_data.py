#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
import ujson as json
import datetime

def database_connection():
    postgresconn = psycopg2.connect("dbname='prop' user='CHANGEME' password='CHANGEME' host='CHANGEME'")
    postgresconn.autocommit = True
    postgrescur = postgresconn.cursor()
    return postgrescur, postgresconn

def delete_potential_victim_data():
	postgrescur, postgresconn = database_connection()
	postgrescur.execute("SELECT username FROM users WHERE primary_class = 'potential_victim' ORDER BY random();")
	all_scraped_users = postgrescur.fetchall()
	for user in all_scraped_users:
		user = user[0]
		print(user)
		postgrescur.execute('DELETE FROM hashtags WHERE hashtag_user = %s;', (user,))
		postgrescur.execute('DELETE FROM links WHERE link_user = %s;', (user,))
	postgrescur.close()
	postgresconn.close()	
	return


delete_potential_victim_data()