# The Small Bot Army Propping Up Trump's Social Influence

## Premise

Accounts that post on social media in a high frequency and automated fashion - often called "bots" - have been a problem for social media companies from the beginning of their existence. Most bots promote spam, scams, malware, and other nefarious for-profit activities, however the 2010s have seen the advent of widespread bot activity in the political sphere. 

The Open Propaganda Framework project asked two key questions: 

1) How many bots are supporting Trump's campaign and what are they talking about? 
2) How much influence do these bots actually have?

The collection and analysis of 1,000,000 Twitter accounts that heavily focused on known propaganda sources gave us a unique insight into answering these two questions. 

## Data Extraction

The /data/trump_bots.csv file contains the data extraction we will be using for this analysis. The method of filtering relied on the following rules:

* Account must be marked "likely_automated=True", which means they are tweeting over 63 times a day on average + they are "Favoriting" 75 tweets per day on average. 
* Account must have at least one point in the "promote_trump" classification
* Account must not be marked "Suspended"

## Question 1: Number of Bots and Topics

We have identified **4916 Twitter accounts** that are tweeting pro-Trump messaging and have a high probability of being automated. Out of a total corpus of one million total accounts, this is a surprisingly small number - representing half a percentage of the population. These accounts are highly visible, noisy, and easy to detect, so our understanding is that these accounts do not last long before being suspended by Twitter. 

In fact, this hypothesis that these accounts are quickly suspended by Twitter may be correct. The median age of these accounts is only 587 days, which means a broad majority of accounts were created in 2017 and 2018. The below image shows how this data is skewed toward newer accounts. 

(https://github.com/OpenPropagandaFramework/opf/blob/master/img/trumpbotage.jpg)

Outside of the typical #MAGA or #Trump2020 tweets, what are these bots talking about? Well, it turns out they more often than not are tweeting radical conspiracy theories like QAnon, Pizzagate, and others. These accounts more often than not link to dubious fake news sources such as the Gateway Pundit, qmap.pub, Trump-Train.com, ilovemyfreedom.org, and TheBlaze. See below for the breakdown of classifications for this pro-Trump bots.

It can be speculated that these accounts are tweeting across a broad variety of topics and linking back to radical conspiracy theories in order to radicalize certain population segments. The profiles of these accounts, combined with the raw links they share, have a ton of references to radical YouTube accounts, 8Chan content, and Gab topics which are trying to radicalize individuals online.

![]((https://github.com/OpenPropagandaFramework/opf/blob/master/img/trumpbottopic.jpg))

Nearly a third of the accounts in this data sample (1548 total) have tweeted Russian media sources directly. Most of these accounts have the occasional link to the Russian state sponsored media source rt.com, however some of these accounts are actively tweeting rt.com daily.

Most of these accounts just retweet other users. A sampling of a couple accounts show retweet percentages as high as 95%, which means these accounts are serving as a platform to get certain hashtags to trend and reach a larger audience. Their engagement rates are fairly low on a per-tweet basis, but that is expected with accounts that tweet hundreds of times a day. 

One confirming indicator that these accounts are largely automated bots of dubious origin is the fact that they do not have geotagged tweets associated with their account. Only 116 of the 4916 accounts have any geotagged locations on their tweets - but even then - most of those geotags are from the "WhiteHouse" or other strange locations. 

The median number of tweets per day for these accounts is 112.6, which is 10-20x the median for the general population of Twitter. The median likes/favorites per day is even higher - 126 - which is even more abnormal compared to the typical Twitter user. The data indicates that these accounts are automated to like certain hashtags, links, or pieces of content in order to recruit new followers. 


## Question 2: Bot Reach and Influence

The **total number of followers for these accounts is a whopping 41.5 MILLION** accounts. This number includes duplicate followers and it is possible that all of these accounts are following each other. If we assume that these roughly 5000 accounts are all following each other (a rough check shows this is not true), then that still leaves the total reach close to 25 million Twitter users. 

Breaking down these numbers further, these accounts get new followers at roughly 7 accounts per day. Surprisingly, they also follow back roughly 7 accounts per day. This may be an automated strategy whereby these accounts will follow other accounts in an attempt to get a follow back. The median number of followers and accounts following per account is 4000, alluding that these accounts are actively controlling their Follower:Following ratio. 

Based on the content analysis above, it would appear that a large proportion of these accounts are designed to automatically retweet certain messages in a coordinated fashion to abuse Twitter's trending algorithms. 



