> NOTICE: The Open Propaganda Framework does not have a social media presence. Please report/ignore impostor accounts on social media. 

# Open Propaganda Framework

The Open Propaganda Framework is an open source framework, toolset, and analysis aggregation point that is focused on political propaganda on social media websites. The goal of The Open Propaganda Project is to be completely collaborative - you are free to expand the toolset, submit new Indicators for analysis, or contribute statistical analysis on the data. All of the code and data in this repository is considered public - hence the MIT license!

The Open Propaganda Project is an attempt to take known techniques used in Cyber Security and apply them to the new world of propaganda based Cyber Warfare. We use atomic Indicators of Compromise (IoCs) in order to analyze content across social media and give accounts a score that represents how likely that account is part of a propaganda influence campaign. The team has found that this approach is actually very successful - not only can we track what new content propagandists are pushing, but we can also discern active propagandists against normal social media users. 

The Open Propaganda Project was born out of a collective frustration with malicious actors manipulating social media to push political agendas. Social media websites are doing a poor job moderating their platforms - to the point where most of our submissions to their content abuse teams falls on deaf ears. This project is an attempt to raise awareness to the size and scope of the active propaganda campaigns on social media, but also is a call to Twitter, Facebook, YouTube, and Reddit to create better ways to detect this kind of content in the future. 

We are taking precautions to conceal our identities - mostly because we do not want to wind up as collateral damage in a larger cyber war amongst nation states. [Other researchers have been targeted with threats of violence, doxxing, and reputational damage,](https://twitter.com/akrolla47/status/1141521590225711105) so we are going to avoid that.

# The Method / Framework

There exists a concept known as [Indicators of Compromise](https://en.wikipedia.org/wiki/Indicator_of_compromise) in the Cyber Security world that we hoped to port over to large-scale analysis of social media. We have three IoC models today based on atomic URLs, domains, and hashtags. Creating a pull request to add additional IoCs is strongly encouraged. We believe the next step forward will be adding a new IoC model based on images, as most of these propaganda accounts share memes/images more often than links or hashtags. 

* [Current Domain IoC List]()
* [Current URL IoC List]()
* [Current Hashtag IoC List]()


We can use these IoCs to then look at accounts for known propaganda activities. For example, we can assume that if an account is sharing thousands of rt.com (Russia Today) articles, then there is a high likelihood they are working in the interests of Russian Media. We can also identify potential victims of propaganda using this model - as they will be sharing a wide variety of known propaganda at slow inconsistent rates. 

Each account is given a total "prop_score", alongside individual propaganda category scores. For example, an account may share some left_voter_suppression tagged IoCs like #blexit, then tweet a promote_trump tagged IoC like #KAG2020.

Another interesting datapoint to note is the "likely automated" flag on each account. Accounts who pass certain thresholds - an average of 62 tweets per day and 75 likes per day over the lifetime of their Twitter account - will be flagged as "likely_automated" bots. These numbers were found via experimentation as explained in [this analysis post.]() 

# Analysis

We welcome researchers to submit pull requests with analysis of the data in markdown format! We will provide our own analysis as well - see below for the published analysis.

**General Resources**

* [Indicator of Compromise Experimental Review]()
* [Running List of Publications on Social Media Influence]()

**Project Specific Analysis**

* []()

# Raw Data

We have analyzed one million Twitter accounts - starting with the IRA dataset - to figure out what propagandists are talking about on Twitter. The details of all one million accounts is in this repository for researchers to dig through. The analysis started March 2019 and ended July 2019. Most of the data is metadata from the last 1000 tweets from all one million accounts. This data is not representative of Twitter as a whole, but rather is skewed torward known propaganda sources. 

All data is found in the /data/ directory of this repository. CSV and JSON formats are provided for ease of use. 

**Data Statistics:**

* 1,000,000 Twitter Accounts Analyzed
* 63,000 High Certainty Propagandists Identified (prop_score > 200)
* 410,000 Victims of Propaganda Identified (200 > prop_score > 1)
* 531,000 Accounts exposed to propaganda, but are not sharing it (prop_score = 0) 

![Summary Stats]()

**Data Files Breakdown**

* all_domains: This data was collected from analyzing the last 1000 tweets from each account in the corpus and extracting the domain name from the URL shard. This data summarizes the 40 million links collected from using this method. 
* all_hashtags: Same as above, except each hashtag in a tweet is recorded and summarized in this data. 
* all_urls: Same as above, except with raw URLs being shared. The database export is capped to 750k records due to GitHub size limitations. 
* all_users: These twenty files contain the entire 
* [category.csv]: There are roughly half a dozen specific data excerpts that are specific to a certain propagandist category. For example, left_voter_suppression.csv contains the top accounts that are pushing voter suppression campaigns against Democratic voters. 

# Tools / Code

There are six core Python scripts that allow you to build on this project. These six core scripts are exactly what we used to compile and analyze this dataset over the course of several months. They are divided into three sections: HUNT, SCRAPE, and ANALYZE. 

## Prerequisites

Before you can get started, you need to have a Postgresql instance running with the schema.sql data model applied (see the root of this repository for that schema file). You will also need Python 3 installed alongside pip3, preferably running in a venv. Go ahead and install  tweepy, ujson, tldextract, psycopg2, emoji, requests, and boto3 (optional if using AWS) using pip3 - instructions may differ depending on the platform. 

## HUNT

The Hunt scripts will find accounts and dump them into the Postgres queue table. This queue table is just that - a simple queue that we will leverage later in the SCRAPE scripts section as an input. We can "Hunt" for accounts via two mechanisms: 1) using the Twitter streaming API (stream.py) which searches for live mentions of IoCs, and/or 2) use Twint to use our existing user's followers and following lists to populate our own data. Again, both scripts just enumerate usernames and dump them into the queue table.


## SCRAPE

The Scrape scripts have two major parts: 1) get_twitter_profile.py and 2) get_tweets.py. Both of these scripts are bound by fairly draconian Twitter API rate limits, so there is an option to leverage multiple known API keys. These scripts can be run in parallel or sequentially depending on your level of access to the Twitter API. get_twitter_profile.py will populate the core attributes of the users database, such as how many tweets an account has, when the account joined Twitter, and how many likes that account has. get_tweets.py will scrape the last 200 tweets (by default, is configurable) on the user's timeline and store hashtags, links, and retweets in Postgres tables. 

## ANALYZE

The core Analyze script is score_classify.py. This can be run nonstop against the database given there are no performance constraints on the database. It will loop through the database and update scores and classifications for users based on the information in the links, hashtags, and ioc tables. There are a couple helper scripts in there as well that can be used to clean up the database or insert new IOCs. 

# Classifications

Classifications allow for easy categorical definitions of objectives when it comes to analyzing propaganda accounts. Below is the latest classification definition. 

* **general_conspiracy**: Promotes (largely harmless) general conspiracy theories. Topics like Area 51, Big Foot, MK-Ultra, etc fall into this classification. 
* **radical_conspiracy**: Promotes radical conspiracy theories like QAnon, PizzaGate, Deep State, Clinton Foundation, etc.  
* **right_social_issues**: Promotes anti-immigration, second ammendment rights, and pro-life issues. The IoCs focus on the divisive content found in these issues, while we leave out hashtags that are broader discussion on these important political issues. 
* **right_media**: Promotes right wing media like Fox News or other generally conservative content. 
* **alt_right_media**: Promotes extremist right wing views. 
* **malicious_media**: Media designed to inflame tensions and create political anger. This IoC classification is reserved for sites that primarily spread targeted misinformation, conspiracy theories, and other malicious content. The domains / URLs that get this classification are often known "fake news" websites per several sources (mediamatters, Snopes, etc). 
* **russian_media**: Media known to be from Russian influence sources.
* **radical_platform_migration**: Content that promotes users to move to more radicalized parts of the internet. This is a tactic seen in social media propaganda campaigns where users are lured into radicalized echo chambers controlled by malicious actors. 
* **christian_right**: Targeting Christians with right wing propaganda. 
* **usa_race_relations**: Fosters racial tensions in the USA, which is one of the classic Russian interference campaign objectives. 
* **defend_mike_flynn**: Strangely there is a large push among propagandists to support Michael Flynn. 
* **left_voter_suppression**: Discourages certain broad or specific demographics from voting, being politically active, or engaging with Democrats. 
* **discredit_left**: Influence actions trying to demonize or attack USA Democrats/progressives
* **right_voter_encouragement**: Encourages conservatives to vote.
* **promote_trump**: Promotes Donald Trump's campaign and presidency. 
* **attack_trump**: Attacks Donald Trump in various ways - recently started seeing these trending.  
* **support_republican_campaign**: Actively supporting and amplifying Republican election campaigns in the House and Senate. 
* **discredit_media**: Encourages distrust in media institutions. 
* **propagandist_tools**: Tools and techniques used by propagandists to actively spread their message. 
* **brexit**: Talks about Brexit, usually in a pro-Brexit way. 
* **europe_influence**: European influence campaigns.  
* **venezuela_influence**: Venezuela influence campaigns. 
* **democrat_nonspecific**: Catch all for mentioning Democrats or the DNC without sentiment. Extremely low point value. 
* **canada_influence**: Catch all for mentioning anything Canadian politics without clear objective.
* **usa_influence_nonspecific**: Catch all for mentioning USA Politics without clear objectives. 
* **australia_influence**: Catch all for mentioning Australian politics without clear objectives. 

# Terms and Definitions Used

* **Propaganda:** information, especially of a biased or misleading nature, used to promote or publicize a particular political cause or point of view.
* **Propagandist:** A propagandist is someone who shares propaganda online. The team discourages the usage of the term "troll" because it demeans the serious nature of the threat being posed to the internet and democracy worldwide. A propagandist can be a real person with the best of intentions, but has been radicalized to the point where propaganda is one of the core tenants of their social media presence. 
* **Malicious Propagandist:** A malicious propagandist is a propagandist that has malicious intent. This can include state sponsored foreign actors who are trying to undermine, destabilize, or achieve nefarious political goals in another country. The team discourages trying to establish country attribution to Malicious Propagandists because 1) it is a VERY difficult problem to solve, and 2) there are ways state sponsored actors cover their tracks to lay blame on other non-affiliated countries. 
* **Victim:** A victim is someone who is sharing propaganda inadvertently. These individuals or accounts demonstrate activity that shows they have been influenced by propaganda, but it is not core to their identity. 
* **Potential Victim:** A potential victim is exposed to propaganda in some fashion, but is not actively sharing propaganda content.
* **Indicator of Compromise (IoC):** Indicator of compromise (IoC) in computer forensics is an artifact observed on a network or in an operating system that, with high confidence, indicates a computer intrusion. This definition requires a bit of translation for social media where we cannot obtain forensic artifacts from the network or specific endpoints. An IoC under this project definition is any atomic artifact that may denote some confidence that the actor is a Propagandist. We use hashtags, domains, and specific URLs as atomic IoCs today.
* **Classification:** A classification is applied to IoCs in an attempt to score propaganda in a consistent fashion. There is a huge difference between an account sharing biased media consistently and sharing radicalized or known malicious content. 


# Contact and PGP Signature

If you need to get in contact with the project, please use the email address openpropframework @/AT protonmail.com. Our PGP key is below. 

-----BEGIN PGP PUBLIC KEY BLOCK-----

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
x/S9K+WsET94T22mWr8=
=oQNa
-----END PGP PUBLIC KEY BLOCK-----