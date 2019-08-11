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

def hashtag_exists(hashtag, postgrescur):
    postgrescur.execute("SELECT * FROM ioc_hashtags WHERE ioc_hashtag = %s", (hashtag,))
    return postgrescur.fetchone() is not None

def domain_exists(domain, postgrescur):
    postgrescur.execute("SELECT * FROM ioc_domains WHERE ioc_domain = %s", (domain,))
    return postgrescur.fetchone() is not None

def url_exists(url, postgrescur):
    postgrescur.execute("SELECT * FROM ioc_urls WHERE ioc_url = %s", (url,))
    return postgrescur.fetchone() is not None

def review_raw_hashtags():
	postgrescur, postgresconn = database_connection()
	hashtag_analysis_sql = 'SELECT hashtag, count(*) FROM hashtags GROUP BY hashtag ORDER BY count(*) DESC LIMIT 500'
	postgrescur.execute(hashtag_analysis_sql)
	top_hashtags = postgrescur.fetchall()
	hashtags_list = []
	for hashtag in top_hashtags:
		ioc_exists = hashtag_exists(hashtag[0], postgrescur)
		if ioc_exists == False:
			hashtag_dict = {"hashtag": hashtag[0], "sightings": hashtag[1], "class": "CHANGEME"}
			hashtags_list.append(hashtag_dict)
	print(json.dumps(hashtags_list))
	postgrescur.close()
	postgresconn.close()

def review_raw_domains():
	postgrescur, postgresconn = database_connection()
	domain_analysis_sql = 'SELECT link_domain, count(*) FROM links GROUP BY link_domain ORDER BY count(*) DESC LIMIT 500'
	postgrescur.execute(domain_analysis_sql)
	top_domains = postgrescur.fetchall()
	domains_list = []
	for domain in top_domains:
		ioc_exists = domain_exists(domain[0], postgrescur)
		if ioc_exists == False:
			domains_dict = {"domain": domain[0], "sightings": domain[1], "class": "CHANGEME"}
			domains_list.append(domains_dict)
	print(json.dumps(domains_list))
	postgrescur.close()
	postgresconn.close()

def review_raw_urls():
	postgrescur, postgresconn = database_connection()
	url_analysis_sql = 'SELECT link_url, count(*) FROM links GROUP BY link_url ORDER BY count(*) DESC LIMIT 500'
	postgrescur.execute(url_analysis_sql)
	top_urls = postgrescur.fetchall()
	urls_list = []
	for url in top_urls:
		ioc_exists = url_exists(url[0], postgrescur)
		if ioc_exists == False:
			url_dict = {"url": url[0], "sightings": url[1], "class": "CHANGEME"}
			urls_list.append(url_dict)
	print(json.dumps(urls_list))
	postgrescur.close()
	postgresconn.close()


review_raw_hashtags()
#review_raw_domains()
#review_raw_urls()
