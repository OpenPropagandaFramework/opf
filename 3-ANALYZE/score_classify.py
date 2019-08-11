#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
import ujson as json
import datetime
import collections


def database_connection():
    postgresconn = psycopg2.connect("dbname='prop' user='CHANGEME' password='CHANGEME' host='CHANGEME'")
    postgresconn.autocommit = True
    postgrescur = postgresconn.cursor()
    return postgrescur, postgresconn

def score_and_classify():
	postgrescur, postgresconn = database_connection()
	postgrescur.execute("SELECT ioc_hashtag, ioc_classification, ioc_weight FROM ioc_hashtags;")
	all_hashtag_iocs = postgrescur.fetchall()
	postgrescur.execute("SELECT ioc_domain, ioc_classification, ioc_weight FROM ioc_domains;")
	all_domain_iocs = postgrescur.fetchall()
	postgrescur.execute("SELECT ioc_url, ioc_classification, ioc_weight FROM ioc_urls;")
	all_url_iocs = postgrescur.fetchall()
	postgrescur.execute("SELECT username FROM users WHERE (status = 'active' or status is null) AND num_of_tweets > 100 ORDER BY random();")
	all_scraped_users = postgrescur.fetchall()
	for user in all_scraped_users:
		user = user[0]
		print(user)
		all_iocs = collections.Counter()
		content_score = 0
		general_conspiracy = 0
		radical_conspiracy = 0
		right_social_issues = 0
		right_media = 0
		alt_right_media = 0
		malicious_media = 0
		russian_media = 0
		radical_platform_migration = 0
		christian_right = 0
		usa_race_relations = 0
		defend_mike_flynn = 0
		left_voter_suppression = 0
		discredit_left = 0
		right_voter_encouragement = 0
		promote_trump = 0
		attack_trump = 0
		support_republican_campaign = 0
		discredit_media = 0
		propagandist_tools = 0
		brexit = 0
		europe_influence = 0
		venezuela_influence = 0
		democrat_nonspecific = 0
		canada_influence = 0
		usa_influence_nonspecific = 0
		australia_influence = 0
		malicious_monetization = 0
		discredit_usa_institutions = 0
		postgrescur.execute("SELECT hashtag FROM hashtags WHERE hashtag_user = %s;", (user,))
		all_hashtags = postgrescur.fetchall()
		for hashtag in all_hashtags:
			san_hash = hashtag[0]
			for iocs in all_hashtag_iocs:
		 		if san_hash in iocs:
		 			all_iocs.update(hashtag)
		 			if iocs[1] == 'general_conspiracy':
		 				general_conspiracy = general_conspiracy + iocs[2]
		 			if iocs[1] == 'radical_conspiracy':
		 				radical_conspiracy = radical_conspiracy + iocs[2]
		 			if iocs[1] == 'right_social_issues':
		 				right_social_issues = right_social_issues + iocs[2]
		 			if iocs[1] == 'right_media':
		 				right_media = right_media + iocs[2]
		 			if iocs[1] == 'alt_right_media':
		 				alt_right_media = alt_right_media + iocs[2]
		 			if iocs[1] == 'malicious_media':
		 				malicious_media = malicious_media + iocs[2]
		 			if iocs[1] == 'russian_media':
		 				russian_media = russian_media + iocs[2]
		 			if iocs[1] == 'radical_platform_migration':
		 				radical_platform_migration = radical_platform_migration + iocs[2]
		 			if iocs[1] == 'christian_right':
		 				christian_right = christian_right + iocs[2]
		 			if iocs[1] == 'usa_race_relations':
		 				usa_race_relations = usa_race_relations + iocs[2]
		 			if iocs[1] == 'defend_mike_flynn':
		 				defend_mike_flynn = defend_mike_flynn + iocs[2]
		 			if iocs[1] == 'left_voter_suppression':
		 				left_voter_suppression = left_voter_suppression + iocs[2]
		 			if iocs[1] == 'discredit_left':
		 				discredit_left = discredit_left + iocs[2]
		 			if iocs[1] == 'right_voter_encouragement':
		 				right_voter_encouragement = right_voter_encouragement + iocs[2]
		 			if iocs[1] == 'promote_trump':
		 				promote_trump = promote_trump + iocs[2]
		 			if iocs[1] == 'attack_trump':
		 				attack_trump = attack_trump + iocs[2]
		 			if iocs[1] == 'support_republican_campaign':
		 				support_republican_campaign = support_republican_campaign + iocs[2]
		 			if iocs[1] == 'discredit_media':
		 				discredit_media = discredit_media + iocs[2]
		 			if iocs[1] == 'propagandist_tools':
		 				propagandist_tools = propagandist_tools + iocs[2]
		 			if iocs[1] == 'brexit':
		 				brexit = brexit + iocs[2]
		 			if iocs[1] == 'europe_influence':
		 				europe_influence = europe_influence + iocs[2]
		 			if iocs[1] == 'venezuela_influence':
		 				venezuela_influence = venezuela_influence + iocs[2]
		 			if iocs[1] == 'democrat_nonspecific':
		 				democrat_nonspecific = democrat_nonspecific + iocs[2]
		 			if iocs[1] == 'canada_influence':
		 				canada_influence = canada_influence + iocs[2]
		 			if iocs[1] == 'usa_influence_nonspecific':
		 				usa_influence_nonspecific = usa_influence_nonspecific + iocs[2]
		 			if iocs[1] == 'australia_influence':
		 				australia_influence = australia_influence + iocs[2]
		 			if iocs[1] == 'malicious_monetization':
		 				malicious_monetization = malicious_monetization + iocs[2]
		 			if iocs[1] == 'discredit_usa_institutions':
		 				discredit_usa_institutions = discredit_usa_institutions + iocs[2]
		 		else:
		 			pass
		postgrescur.execute("SELECT link_domain FROM links WHERE link_user = %s;", (user,))
		all_domains = postgrescur.fetchall()
		for domain in all_domains:
			san_domain = domain[0]
			for iocs in all_domain_iocs:
		 		if san_domain in iocs:
		 			all_iocs.update(domain)
		 			if iocs[1] == 'general_conspiracy':
		 				general_conspiracy = general_conspiracy + iocs[2]
		 			if iocs[1] == 'radical_conspiracy':
		 				radical_conspiracy = radical_conspiracy + iocs[2]
		 			if iocs[1] == 'right_social_issues':
		 				right_social_issues = right_social_issues + iocs[2]
		 			if iocs[1] == 'right_media':
		 				right_media = right_media + iocs[2]
		 			if iocs[1] == 'alt_right_media':
		 				alt_right_media = alt_right_media + iocs[2]
		 			if iocs[1] == 'malicious_media':
		 				malicious_media = malicious_media + iocs[2]
		 			if iocs[1] == 'russian_media':
		 				russian_media = russian_media + iocs[2]
		 			if iocs[1] == 'radical_platform_migration':
		 				radical_platform_migration = radical_platform_migration + iocs[2]
		 			if iocs[1] == 'christian_right':
		 				christian_right = christian_right + iocs[2]
		 			if iocs[1] == 'usa_race_relations':
		 				usa_race_relations = usa_race_relations + iocs[2]
		 			if iocs[1] == 'defend_mike_flynn':
		 				defend_mike_flynn = defend_mike_flynn + iocs[2]
		 			if iocs[1] == 'left_voter_suppression':
		 				left_voter_suppression = left_voter_suppression + iocs[2]
		 			if iocs[1] == 'discredit_left':
		 				discredit_left = discredit_left + iocs[2]
		 			if iocs[1] == 'right_voter_encouragement':
		 				right_voter_encouragement = right_voter_encouragement + iocs[2]
		 			if iocs[1] == 'promote_trump':
		 				promote_trump = promote_trump + iocs[2]
		 			if iocs[1] == 'attack_trump':
		 				attack_trump = attack_trump + iocs[2]
		 			if iocs[1] == 'support_republican_campaign':
		 				support_republican_campaign = support_republican_campaign + iocs[2]
		 			if iocs[1] == 'discredit_media':
		 				discredit_media = discredit_media + iocs[2]
		 			if iocs[1] == 'propagandist_tools':
		 				propagandist_tools = propagandist_tools + iocs[2]
		 			if iocs[1] == 'brexit':
		 				brexit = brexit + iocs[2]
		 			if iocs[1] == 'europe_influence':
		 				europe_influence = europe_influence + iocs[2]
		 			if iocs[1] == 'venezuela_influence':
		 				venezuela_influence = venezuela_influence + iocs[2]
		 			if iocs[1] == 'democrat_nonspecific':
		 				democrat_nonspecific = democrat_nonspecific + iocs[2]
		 			if iocs[1] == 'canada_influence':
		 				canada_influence = canada_influence + iocs[2]
		 			if iocs[1] == 'usa_influence_nonspecific':
		 				usa_influence_nonspecific = usa_influence_nonspecific + iocs[2]
		 			if iocs[1] == 'australia_influence':
		 				australia_influence = australia_influence + iocs[2]
		 			if iocs[1] == 'malicious_monetization':
		 				malicious_monetization = malicious_monetization + iocs[2]
		 			if iocs[1] == 'discredit_usa_institutions':
		 				discredit_usa_institutions = discredit_usa_institutions + iocs[2]
		 		else:
		 			pass
		postgrescur.execute("SELECT link_url FROM links WHERE link_user = %s;", (user,))
		all_links = postgrescur.fetchall()
		for url in all_links:
			san_url = url[0]
			for iocs in all_url_iocs:
		 		if san_url in iocs:
		 			all_iocs.update(url)
		 			if iocs[1] == 'general_conspiracy':
		 				general_conspiracy = general_conspiracy + iocs[2]
		 			if iocs[1] == 'radical_conspiracy':
		 				radical_conspiracy = radical_conspiracy + iocs[2]
		 			if iocs[1] == 'right_social_issues':
		 				right_social_issues = right_social_issues + iocs[2]
		 			if iocs[1] == 'right_media':
		 				right_media = right_media + iocs[2]
		 			if iocs[1] == 'alt_right_media':
		 				alt_right_media = alt_right_media + iocs[2]
		 			if iocs[1] == 'malicious_media':
		 				malicious_media = malicious_media + iocs[2]
		 			if iocs[1] == 'russian_media':
		 				russian_media = russian_media + iocs[2]
		 			if iocs[1] == 'radical_platform_migration':
		 				radical_platform_migration = radical_platform_migration + iocs[2]
		 			if iocs[1] == 'christian_right':
		 				christian_right = christian_right + iocs[2]
		 			if iocs[1] == 'usa_race_relations':
		 				usa_race_relations = usa_race_relations + iocs[2]
		 			if iocs[1] == 'defend_mike_flynn':
		 				defend_mike_flynn = defend_mike_flynn + iocs[2]
		 			if iocs[1] == 'left_voter_suppression':
		 				left_voter_suppression = left_voter_suppression + iocs[2]
		 			if iocs[1] == 'discredit_left':
		 				discredit_left = discredit_left + iocs[2]
		 			if iocs[1] == 'right_voter_encouragement':
		 				right_voter_encouragement = right_voter_encouragement + iocs[2]
		 			if iocs[1] == 'promote_trump':
		 				promote_trump = promote_trump + iocs[2]
		 			if iocs[1] == 'attack_trump':
		 				attack_trump = attack_trump + iocs[2]
		 			if iocs[1] == 'support_republican_campaign':
		 				support_republican_campaign = support_republican_campaign + iocs[2]
		 			if iocs[1] == 'discredit_media':
		 				discredit_media = discredit_media + iocs[2]
		 			if iocs[1] == 'propagandist_tools':
		 				propagandist_tools = propagandist_tools + iocs[2]
		 			if iocs[1] == 'brexit':
		 				brexit = brexit + iocs[2]
		 			if iocs[1] == 'europe_influence':
		 				europe_influence = europe_influence + iocs[2]
		 			if iocs[1] == 'venezuela_influence':
		 				venezuela_influence = venezuela_influence + iocs[2]
		 			if iocs[1] == 'democrat_nonspecific':
		 				democrat_nonspecific = democrat_nonspecific + iocs[2]
		 			if iocs[1] == 'canada_influence':
		 				canada_influence = canada_influence + iocs[2]
		 			if iocs[1] == 'usa_influence_nonspecific':
		 				usa_influence_nonspecific = usa_influence_nonspecific + iocs[2]
		 			if iocs[1] == 'australia_influence':
		 				australia_influence = australia_influence + iocs[2]
		 			if iocs[1] == 'malicious_monetization':
		 				malicious_monetization = malicious_monetization + iocs[2]
		 			if iocs[1] == 'discredit_usa_institutions':
		 				discredit_usa_institutions = discredit_usa_institutions + iocs[2]
		 		else:
		 			pass
		all_iocs = str(all_iocs)
		content_score_dict = {'general_conspiracy': general_conspiracy, 'radical_conspiracy': radical_conspiracy, 'right_social_issues': right_social_issues, 'right_media': right_media, 'alt_right_media': alt_right_media, 'malicious_media': malicious_media, 'russian_media': russian_media, 'radical_platform_migration': radical_platform_migration, 'christian_right': christian_right, 'usa_race_relations': usa_race_relations, 'defend_mike_flynn': defend_mike_flynn, 'left_voter_suppression': left_voter_suppression, 'discredit_left': discredit_left, 'right_voter_encouragement': right_voter_encouragement, 'promote_trump': promote_trump, 'attack_trump': attack_trump, 'support_republican_campaign': support_republican_campaign, 'discredit_media': discredit_media, 'propagandist_tools': propagandist_tools, 'brexit': brexit, 'europe_influence': europe_influence, 'venezuela_influence': venezuela_influence, 'democrat_nonspecific': democrat_nonspecific, 'canada_influence': canada_influence, 'usa_influence_nonspecific': usa_influence_nonspecific, 'australia_influence': australia_influence, 'malicious_monetization': malicious_monetization, 'discredit_usa_institutions': discredit_usa_institutions}
		content_score = general_conspiracy+radical_conspiracy+right_social_issues+right_media+alt_right_media+malicious_media+russian_media+radical_platform_migration+christian_right+usa_race_relations+defend_mike_flynn+left_voter_suppression+discredit_left+right_voter_encouragement+promote_trump+attack_trump+support_republican_campaign+discredit_media+propagandist_tools+brexit+europe_influence+venezuela_influence+democrat_nonspecific+canada_influence+usa_influence_nonspecific+australia_influence+malicious_monetization+discredit_usa_institutions
		if content_score == 0:
			primary_class = 'potential_victim'
		else:
			primary_class = max(content_score_dict, key=content_score_dict.get)
		postgrescur.execute('UPDATE users SET content_score = %s, general_conspiracy = %s, radical_conspiracy = %s, right_social_issues = %s, right_media = %s, alt_right_media = %s, malicious_media = %s, russian_media = %s, radical_platform_migration = %s, christian_right = %s, usa_race_relations = %s, defend_mike_flynn = %s, left_voter_suppression = %s, discredit_left = %s, right_voter_encouragement = %s, promote_trump = %s, attack_trump = %s, support_republican_campaign = %s, discredit_media = %s, propagandist_tools = %s, brexit = %s, europe_influence = %s, venezuela_influence = %s, democrat_nonspecific = %s, canada_influence = %s, usa_influence_nonspecific = %s, australia_influence = %s, malicious_monetization = %s, discredit_usa_institutions = %s, all_iocs = %s, primary_class = %s WHERE username = %s;', (content_score,general_conspiracy,radical_conspiracy,right_social_issues,right_media,alt_right_media,malicious_media,russian_media,radical_platform_migration,christian_right,usa_race_relations,defend_mike_flynn,left_voter_suppression,discredit_left,right_voter_encouragement,promote_trump,attack_trump,support_republican_campaign,discredit_media,propagandist_tools,brexit,europe_influence,venezuela_influence,democrat_nonspecific,canada_influence,usa_influence_nonspecific,australia_influence,malicious_monetization,discredit_usa_institutions,all_iocs,primary_class,user))
	postgrescur.close()
	postgresconn.close()

score_and_classify()
