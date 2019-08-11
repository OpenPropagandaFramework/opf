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

def process_review_hashtags():
	postgrescur, postgresconn = database_connection()
	very_low_score_class = ['right_media', 'christian_right', 'right_social_issues', 'democrat_nonspecific']
	low_score_class = ['alt_right_media', 'right_voter_encouragement', 'promote_trump', 'attack_trump', 'propagandist_tools', 'brexit', 'canada_influence', 'usa_influence_nonspecific', 'australia_influence']
	medium_score_class = ['general_conspiracy', 'usa_race_relations', 'discredit_left', 'support_republican_campaign', 'discredit_media', 'europe_influence', 'venezuela_influence', 'discredit_usa_institutions']
	high_score_class = ['radical_conspiracy', 'malicious_media', 'russian_media', 'radical_platform_migration', 'defend_mike_flynn', 'left_voter_suppression', 'malicious_monetization']
	now = datetime.datetime.now()
	review_data = ''
	review_json = json.loads(review_data)
	for indicator in review_json:
		ioc_hashtag = indicator['hashtag']
		ioc_sightings = indicator['sightings']
		ioc_class = indicator['class']
		if ioc_class in very_low_score_class:
			ioc_weight = 1
		if ioc_class in low_score_class:
			ioc_weight = 2
		if ioc_class in medium_score_class:
			ioc_weight = 3
		if ioc_class in high_score_class:
			ioc_weight = 5
		try:
			if ioc_weight:
				pass
		except:
			ioc_weight = 0
		postgrescur.execute("INSERT INTO ioc_hashtags (ioc_hashtag, ioc_sightings, ioc_weight, ioc_classification) VALUES (%s, %s, %s, %s) ON CONFLICT (ioc_hashtag) DO NOTHING;", (ioc_hashtag, ioc_sightings, ioc_weight, ioc_class))
	postgrescur.close()
	postgresconn.close()
	return

def process_review_domains():
	postgrescur, postgresconn = database_connection()
	very_low_score_class = ['right_media', 'christian_right', 'right_social_issues', 'democrat_nonspecific']
	low_score_class = ['alt_right_media', 'right_voter_encouragement', 'promote_trump', 'attack_trump', 'propagandist_tools', 'brexit', 'canada_influence', 'usa_influence_nonspecific', 'australia_influence']
	medium_score_class = ['general_conspiracy', 'usa_race_relations', 'discredit_left', 'support_republican_campaign', 'discredit_media', 'europe_influence', 'venezuela_influence', 'discredit_usa_institutions']
	high_score_class = ['radical_conspiracy', 'malicious_media', 'russian_media', 'radical_platform_migration', 'defend_mike_flynn', 'left_voter_suppression', 'malicious_monetization']
	now = datetime.datetime.now()
	review_data = ' '	
	review_json = json.loads(review_data)
	for indicator in review_json:
		ioc_domain = indicator['domain']
		ioc_sightings = indicator['sightings']
		ioc_class = indicator['class']
		if ioc_class in very_low_score_class:
			ioc_weight = 1
		if ioc_class in low_score_class:
			ioc_weight = 2
		if ioc_class in medium_score_class:
			ioc_weight = 3
		if ioc_class in high_score_class:
			ioc_weight = 5
		try:
			if ioc_weight:
				pass
		except:
			ioc_weight = 0
		postgrescur.execute("INSERT INTO ioc_domains (ioc_domain, ioc_sightings, ioc_weight, ioc_classification) VALUES (%s, %s, %s, %s) ON CONFLICT (ioc_domain) DO NOTHING;", (ioc_domain, ioc_sightings, ioc_weight, ioc_class))
	postgrescur.close()
	postgresconn.close()
	return

def process_review_urls():
	postgrescur, postgresconn = database_connection()
	very_low_score_class = ['right_media', 'christian_right', 'right_social_issues', 'democrat_nonspecific', 'left_media']
	low_score_class = ['alt_right_media', 'right_voter_encouragement', 'promote_trump', 'attack_trump', 'propagandist_tools', 'brexit', 'canada_influence', 'usa_influence_nonspecific', 'australia_influence']
	medium_score_class = ['general_conspiracy', 'usa_race_relations', 'discredit_left', 'support_republican_campaign', 'discredit_media', 'europe_influence', 'venezuela_influence', 'discredit_usa_institutions']
	high_score_class = ['radical_conspiracy', 'malicious_media', 'russian_media', 'radical_platform_migration', 'defend_mike_flynn', 'left_voter_suppression', 'malicious_monetization']
	now = datetime.datetime.now()
	review_data = '	'
	review_json = json.loads(review_data)
	for indicator in review_json:
		ioc_url = indicator['url']
		ioc_sightings = indicator['sightings']
		ioc_class = indicator['class']
		if ioc_class in very_low_score_class:
			ioc_weight = 1
		if ioc_class in low_score_class:
			ioc_weight = 2
		if ioc_class in medium_score_class:
			ioc_weight = 3
		if ioc_class in high_score_class:
			ioc_weight = 5
		try:
			if ioc_weight:
				pass
		except:
			ioc_weight = 0
		postgrescur.execute("INSERT INTO ioc_urls (ioc_url, ioc_sightings, ioc_weight, ioc_classification) VALUES (%s, %s, %s, %s) ON CONFLICT (ioc_url) DO NOTHING;", (ioc_url, ioc_sightings, ioc_weight, ioc_class))
	postgrescur.close()
	postgresconn.close()
	return

process_review_hashtags()
#process_review_domains()
# process_review_urls()

