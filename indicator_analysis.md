# Indicator of Compromise (IoC) Evidence

An Indicator of Compromise (IoC) is an atomic indicator that an account may be known propaganda. The below lays out evidence around different IoC metrics and how they were tested for validity. I encourage others to run their own tests to validate these IoCs and provide additional evidence that validates or disputes the findings below. 

# Twitter Indicators of Compromise (IoC)

## Methods of Testing

Tweepy was used to collect this data via a Python script. All account information provided by the Twitter API via Tweepy was analyzed for abnormalities, along with a sampling of the last 1000 tweets for each user. The team tested three different groups of Twitter users to determine statistical relevance of certain potential indicators. 

Control Group #1 ("Lawn Group") was collected by searching for accounts who tweeted the phrase "mowing my lawn" in the month of May 2019. There were 891 accounts retrieved worldwide after pruning accounts that had included political words, hashtags, or phrases in their description. This control group is considered a wide representation of potential normal Twitter users that are not geo-boxed in any way. n=891 for the "Lawn Group". 

Control Group #2 ("Whiteboard Group") was collected by searching for accounts that matched the following criteria: 1) geo-tagged as being in the New York City metro area, and 2) the account tweeted the term "whiteboard" in the month of May 2019. This population of users largely represented employees working in technology, marketing, and sales in the New York City area. Some of these accounts are automated marketing / sales accounts, which was a good sample to test against for engagement metrics. n=439 for the "Whiteboard Group".

The Experimental Group ("Suspected Propagandists") was collected by searching for accounts that tweeted hashtags that have been suspected as being Propagandist-specific hashtags. The following hashtags were used to collect accounts tweeting these hashtags in real-time using the Twitter streaming API: '#TheGreatAwakening', '#PatriotsFight', '#WWG1WGA', '#PatriotsAwakened', '#UCzsvtAGvvbs64k', '#DOITQ', '#WalkAway'. n=129 total accounts were collected via this method by streaming and de-duplicating accounts tweeting these hashtags over the course of a random day in May 2019. This group is assumed to have a large population of Propagandists, but the goal is to disprove this hypothesis. 

The total number of accounts analyzed across all three groups was 1459, which reaches statistical significance. A larger study should be done to understand variance.

## Indicator of Compromise for Twitter Statistical Review

The following will outline the findings of the analysis of these 1459 Twitter accounts differentiated by Grouping. The findings will be grouped by the statistical strength of the findings. A method of programmatically scoring these IoCs is presented within each statistically significant IoC in order to scale out this analysis to a larger population. 

The following method has been developed to determine a total "Account Score" that combines several IoC scores to determine a total weight. This "Account Score" only uses metadata data gathered through the account's Twitter profile without examining tweet contents. The method to calculate "Account Score" is to sum the scores around "IOC1: Blacklist Hashtag in Account Bio", "IOC2: Average New Following Per Day", "IOC3: Average New Followers Per Day", and "IOC4: Average New Likes Per Day". 

### Very Strong Indicators of Compromise

1. **IOC1: Number of Blacklist Hashtags in Account Bio**
	* Description: The hypothesis was tested that Propagandist Twitter accounts use politically charged and coordinated hashtags in their Twitter Account biography/description section. Normal users don't tend to have highly political hashtags in their descriptions, but instead tend to elect for more personal descriptors. The hypothesis was strongly confirmed that searching for accounts with politically charged hashtags in their descriptions led to a higher assurance that the account is a Propagandist.
	* Social Network: Twitter Profile
	* Strength: Very Strong Indicator
		* Rationale: Very low false positive rate with a high prediction rate. This indicator will improve as a more comprehensive and updated list of Propagandist hashtags is discovered. 
	* Evidence:
		* Lawn Group: 4/891 (0.58%) of Accounts Contained Blacklist Hashtags. 
			katehelms
			k_dani12
			beetle6321
			hyzermike
			clarkke95563197
			maryellen3261
		* Whiteboard Group: 0/439 (0%) of Accounts Contained Blacklist Hashtags.
		* Suspected Propagandists: The statistics below are based on the number of Blacklist hashtags seen.
			* Average: 1.01
			* Median: 0.0
			* 10% Percentile: 0.0
			* 90% Percentile: 3.0
			* Standard Deviation: 1.321
	* Scoring: 200pts
		* High Assurance: Metric >= 3
			* Score = 200
		* Medium Assurance: Metric = 2
			* Score = 150
		* Low Assurance: Metric = 1
			* Score = 100
		* Score equals zero if no blacklist hashtags are seen.
2. **IOC2: Average New Following Per Day**
	* Description: Suspected Propagandists follow fifteen times more accounts per day than any other sampling of normal Twitter users. Propagandists seem to have figured out that following more accounts leads to more followers back, which leads to more overall social reach. This has been a classic Twitter marketing tactic for quite a long time, however Suspected Propagandists even out-pace the marketing heavy control group in this regard. 
	* Social Network: Twitter Profile
	* Strength: Very Strong Indicator
	* Evidence: All measures are average new following accounts per day. 
		* Whiteboard Group:
			* Average: 0.491
			* Median: 0.12
			* 10% Percentile: 0.046
			* 90% Percentile: 0.913
			* Standard Deviation: 1.633
		* Lawn Group: 
			* Average: 0.852
			* Median: 0.219
			* 10: 0.047
			* 90: 1.367
			* Standard Deviation: 3.56
		* Suspected Propagandists:
			* Average: 14.146
			* Median: 6.245
			* 10: 0.95
			* 90% Percentile: 44.03
			* Standard Deviation: 20.441
	* Scoring: 200pts
		* Very High: Metric > 20 Per Day
			* Score: 200
		* High: Metric >20 Per Day
			* Score 150
		* Medium: Metric >10 Per Day
			* Score 75
		* Medium-Low: Metric > 6 Per Day
			* Score 50
		* Low: Metric > 3 Per Day
			* Score 25
3. **IOC3: Average Likes Per Day**
	* Description: Suspected propagandists "like" content on Twitter ten times more often than any other sampling of normal Twitter users. Similar to the Following metric, this seems to be linked to increased social reach on Twitter by: 1) validating propaganda spread by Propagandists as well as Radicals, but also 2) increasing likelihood that they will gain followers through being higher visibility. 
	* Social Network: Twitter Profile
	* Strength: Very Strong Indicator
	* Evidence: All measures are average new likes per day.
		* Whiteboard Group: 
			* Average: 3.08
			* Median: 0.87
			* 10% Percentile: 0.031
			* 90% Percentile: 7.481
			* Standard Deviation: 6.89
		* Lawn Group:
			* Average: 11.499
			* Median: 2.795
			* 10: 0.147
			* 90: 27.29
			* Standard Deviation: 30.895
		* Suspected Propagandists: 
			* Average: 55.534
			* Median: 29.12
			* 10% Percentile: 3.053
			* 90% Percentile: 133.827
			* Standard Deviation: 75.857
	* Scoring (Weight:200)
		* High: Metric > 120 Per Day
			* Score: 200
		* Medium: Metric >75 Per Day
			* Score 150
		* Low: Metric >50 Per Day
			* Score 100
4. **IOC7: Profile is Verified**
	* Description: Twitter Verified accounts are relatively difficult to obtain and require some sort of identity validation. While a verified account can spread propaganda, the team decided to exclude them from classification. The negative score will highlight whether Verified Twitter accounts are spreading known propaganda through deductions from their base negative score of -10,000
	* Social Network: Twitter Profile
	* Strength: Very Strong Reverse Indicator
	* Scoring:
		* If True: -10000pts
		* If False: No Change

### Strong Indicators of Compromise

1. **IOC4: Average Tweets Per Day Since Account Creation**
	* Description: Propagandist accounts spread their message through pure brute force - they tweet ten times more than the median of normal Twitter users. I suspect that this IoC will have a much larger false positive rate at scale, however this should be mitigated through weighting it against stronger indicators. Suspected Propagandists: 10x Median, 5x Average, 7x 90% Percentile. 
	* Social Networks: Twitter Profile
	* Indicator Strength: Strong 
	* Evidence: All numbers represent average tweets per day since account creation
		* Lawn Group
			* Average: 10.08
			* Median: 3.55
			* 10% Percentile: 0.446
			* 90% Percentile: 22.491
			* Standard Deviation: 26.195
		* Whiteboard Group
			* Average: 5.59
			* Median: 2.01
			* 10% Percentile: 0.328
			* 90% Percentile: 12.865
			* Standard Deviation: 11.75
		* Suspected Propagandists:
			* Average: 56.899
			* Median: 32.445
			* 10% Percentile: 3.17
			* 90% Percentile: 141.5695
			* Standard Deviation: 69.817
	* Scoring: 100pts
		* Very High: Metric > 88
			* Score = 100
		* High: Metric > 63
			* Score = 75
		* Medium: Metric > 32
			* Score = 50
		* Low: Metric > 23
			* Score = 25
2. **IOC5: Average New Followers Per Day** 
	* Description: Average New Followers Per Day measures the rate that accounts get new followers per day. More followers mean more potential social reach, so this is an important measure of success for Propagandists. The team suspects that there may be "clustering" occurring where Propagandists follow each other to gain legitimacy and further spread their message. Propagandists also tend to participate in "follow chains" that encourage users to follow each other by using similar hashtags. The rate that Suspected Propagandists get new followers was twenty four times greater than normal Twitter users. 
	* Social Networks: Twitter Profile
	* Indicator Strength: Strong Indicator
	* Evidence
		* Whiteboard Group
			* Average: 1.66
			* Median: 0.248
			* 10% Percentile: 0.038
			* 90% Percentile: 2.738
			* Standard Deviation: 8.796
		* Lawn Group
			* Average: 0.925
			* Median: 0.1799
			* 10% Percentile: 0.0256
			* 90% Percentile: 1.585
			* Standard Deviation: 3.867
		* Suspected Propagandists
			* Average: 13.659
			* Median: 5.95
			* 10% Percentile: 0.91
			* 90% Percentile: 42.78
			* Standard Deviation: 19.886
	* Scoring: 100pts
		* Very High: Metric > 40
			* Score = 100
		* High: Metric > 30
			* Score = 75
		* Medium: Metric > 20
			* Score = 50
		* Low: Metric > 10
			* Score = 25
3. **IOC6: Emojis in Name and Description + Hashtag in Description**
	* Description: This indicator resolves as "True" when there is an emoji in the "Name" and "Biography/Description" fields in the Twitter profile, combined with there being any hashtag in the description. This indicator was a bit of a surprise - the usage of emojis in these user-set fields in Twitter was seen anecdotally, but it was surprisingly statistically significant. Propagandists may use this to make their profiles "pop" out to normal users on the Twitter feed, since emojis are eye catching. No analysis was done on what types of emojis were used, however that is a good area for future research. False positive rate is surprisingly low, however only 18% of Suspected Propagandist accounts displayed these characteristics, so it is not quite a "Very Strong" indicator.
	* Social Networks: Twitter Profile
	* Indicator Strength: Strong indicator. 
	* Evidence:
		* Lawn Group
			* 8/891 Resolved True, which is a 0.9% hit percentage. No analysis has been done on whether these are false positives or true positives. 
		* Whiteboard Group
			* 4/439 Resolved True, which is also a 0.9% hit percentage. No analysis has been done on whether these are false positives or true positives. 
		* Suspected Propagandists
			* 25/129 Resolved True, which is a 19.37% hit rate. 
	* Scoring: 100pts
		* If Profile Resolves True = +100
		* If Profile Resolves False = 0
4. **IOC9: Average User Score of Retweeted Accounts**
	* Description: This indicator focuses on statistical ananlysis of an account's retweets. Twitter is kind enough to provide the full user profile of the account that was retweeted, so we can perform a quick Account Score analysis of that account. From our observational data it is clear that Propagandists tend to retweet other Propagandist content - operating in interconnected clusters of accounts. This indicator therefore analyzes the Account Score of the account whose content was shared - these scores are averaged out over _n_ number of retweets to get a composite IOC metric. 
	Troll: Average: 226.68178571428572, Median: 150.0, 10: 1.0, 90: 600.0, std: 225.24687208155746
	Lawn: Average: 17.40636695018226, Median: 1.0, 10: 0.0, 90: 50.0 std: 57.082549576423204



### Moderate Indicators of Compromise

1. **IOC8: Profile Contains URL**
	* Description: This indicator is a boolean "True" or "False" now, but can be refined based on URL analysis. This indicator resolves "True" if an account has a URL associated with their Twitter account. This indicator was an unexpected result of the team's statistical analysis due to assumptions that Propagandists would want to lead normal users to more radicalized areas of the internet. 
	* Social Networks: Twitter Profile
	* Indicator Strength: Moderate Reverse Indicator
	* Evidence
		* Lawn Group
			* 290/891 Resolved True, which means 32.5% of normal users have URLs associated with their Twitter accounts.
		* Whiteboard Group
			* 300/439 Resolved True, which means 68.3% of normal (marketing/tech) users have URLs associated with their Twitter accounts.
		* Suspected Propandists
			* 14/129 Resolved True, which means 10.9% of Suspected Propagandists have URLs associated with their Twitter accounts. Out of those 14 "True" results, 9 of them were manually confirmed to be a political propaganda website. The resulting 5 accounts that resolved "True" were links to eBay shops, Etsy shops, and other personal links that provide assurance they are real non-malicious Propagandists. 
	*Scoring: 50pts
		* If Profile Contains Link = -50
		* If Profile Does Not Contain Link = 0
2. **IOC10: Total Retweet Percentage**
	* Description: The amount of retweets from the Suspected Propaganda accounts is a staggering 80% of sampled tweets from those accounts. The normal retweet percentage is closer to 20%, so this can be used as a moderate indicator of Propagandist activity. The strength of this indicator is moderate due to the amount of potential false positives in individual user activity. 
		Lawn: Counter({False: 15786, True: 4789}) 23% RTs
		Trolls: Counter({True: 11130, False: 2870}) 80% RTs





### Weak Indicators of Compromise

These indicators are not implemented in the total scoring due to potential for false positives. These are here as references for future researchers to understand how these attributes stacked up in our analysis. 

1. **Geo + Extended Profile**
	Medium Indicator: Geo Tagged Profile + Extended Profile together are seen 2x+ more in normal people vs. Trolls. Might be a good validator.
	Whiteboard: Counter({False: 296, True: 143}) 29%
	Lawn: Counter({False: 624, True: 261}) 33%
	Trolls: Counter({False: 109, True: 20}) 14%
	Scoring (Weight 50):
		If Profile Contains Geo+Extended = -50
		If Profile Does Not Contain Geo+Extended = 0
2. **Account Age (Days)**
	Medium Indicator: Troll accounts typically half as old as normal accounts
	Lawn: AVERAGE: 2152.0931537598203, MEDIAN: 2318.0, 10: 353.0, 90: 3690.0, stddev: 1183.3827766349239
	Whiteboard: AVERAGE: 3255.9362186788153, MEDIAN: 3607.0, 10: 1925.6000000000001, 90: 4190.4, stddev: 914.3929664377866
	Trolls: AVERAGE: 1669.5116279069769, MEDIAN: 1341.0, 10: 169.8, 90: 3619.8, stddev: 1259.2365542173538
3. **Emojis in Name and Description**
	Medium Indicator: False Positive rate is pretty high, but trolls do have double emojis more often. 
	Lawn: Counter({False: 825, True: 66}) 7%
	Whiteboard: Counter({False: 422, True: 17}) 4%
	Trolls: Counter({False: 93, True: 36}) 26%
4. **User Has Emoji in Twitter Name**
	Moderate indicator - will be prone to false positives. 
	Lawn: Counter({False: 738, True: 153}) 17%
	Whiteboard: Counter({False: 394, True: 45}) 10%
	Trolls: Counter({False: 72, True: 57}) 41%
5. **User Has Emoji in Description/Bio**
	Weak Indicator - Lots of false positives despite trend.
	Lawn: Counter({False: 659, True: 232}) 20%
	Whiteboard: Counter({False: 350, True: 89}) 26%
	Trolls: Counter({True: 69, False: 60}) 55%
6. **Twitter Profile Geolocation**
	WEAK INDICATOR (Trolls slighly less likely to have this set to True)
	Lawn: Counter({False: 461, True: 430}) 50% True
	Whiteboard: Counter({False: 48, True: 391}) 89% True
	Trolls: Counter({False: 83, True: 46}) 35% True
7. **Twitter Extended Profile**
	Weak Indicator
	Lawn: Counter({False: 453, True: 438}) 50% True
	Whiteboard: Counter({False: 277, True: 162}) 37% True
	Troll: Counter({False: 90, True: 39}) 30% True
8. **User Has Hashtag in Description/Bio**
	Moderate Indicator - Will be prone to lots of false positives
	Lawn: Counter({False: 782, True: 109}) 12%
	Whiteboard: Counter({False: 369, True: 70}) 16%
	Trolls: Counter({True: 81, False: 48}) 58%


### Legacy Indicators That Have Been Decommissioned

These indicators have been thrown out due to better normalized indicators being developed, or better composite indicators being developed. For example, Total Tweets was a worse indicator than Tweets Per Day, which is normalized by account age. 

1. Total Number of Accounts User is Following
	Strong Indicator: Trolls follow 9-10x the amount of accounts normal people follow
	Lawn: AVERAGE: 1190.9337822671157, MEDIAN: 400.0, 10: 72.0, 90: 1952.0, stddev: 8822.40203688549
	Whiteboard: AVERAGE: 1327.9817767653758, MEDIAN: 655.0, 10: 128.0, 90%: 2462.7999999999997, stddev: 2914.5137627865156
	Trolls: AVERAGE: 10160.945736434109, MEDIAN: 6055.0, 10: 1367.4, 90: 24118.600000000006, stddev: 10176.907034064978
	Scoring (Weight:100)
		Very High: Metric > 22000
			Score = 100
		High: Metric > 17000
			Score = 75
		Medium: Metric > 6000
			Score = 50
		Low: Metric > 2500
			Score = 25
2. Total Number of Twitter Followers
	Moderate Indicator (Median 5900 for trolls is way above even the skewed averages of normal people)
	False positives will occur due to naturally popular accounts.
	Might want to combine with Following metric. 
	Whiteboard: AVERAGE: 5521.496583143508, MEDIAN: 769.0, 10: 105.60000000000001, 90: 8065.199999999999, stddev: 31501.310193374353
	Lawn: AVERAGE: 1620.0998877665545, MEDIAN: 311.0, 10: 35.0, 90: 2402.0, stddev: 10781.43707618483
	Trolls: AVERAGE: 10085.945736434109, MEDIAN: 5900.0, 10: 1103.0, 90: 23716.000000000007, stddev: 10494.871032523626
3. Total Number of Likes:
	Strong Indicator: Trolls like things 5x more than normal people
	Lawn: AVERAGE: 15701.90684624018, MEDIAN: 5290.0, 10: 230.0, 90: 43037.0, stddev: 29852.420757546588
	Whiteboard: AVERAGE: 9608.439635535307, MEDIAN: 2484.0, 10: 96.0, 90: 24766.999999999993, stddev: 21799.48248461769
	Trolls: AVERAGE: 48495.31007751938, MEDIAN: 24969.0, 10: 3512.4, 90: 131786.6, stddev: 52859.75176007177
4. Total Number of Tweets
	Strong Indicator (Trolls overall tweets 3x normal people, even tech folks who have been on the platform forever)
	Tweets Per Day might be a better metric to score against. 
	Lawn: AVERAGE: 17684.544332211, MEDIAN: 6625.0, 10: 497.0, 90: 41190.0, stddev: 35308.0309752635
	Whiteboard: AVERAGE: 18088.86560364465, MEDIAN: 6820.0, 10: 741.8000000000001, 90: 42445.59999999999, stddev: 35975.11330243683
	Trolls: AVERAGE: 56276.51937984496, MEDIAN: 29934.0, 10: 4753.8, 90: 137692.60000000003, stddev: 76205.47803917942

### Attributes That Aren't Statistically Relevant

1. **User Inputted Location**
	This came as a surprise, since the team was expecting some common pattern for Suspected Propagandists in relation to the user-defined profile location value. There may be a pattern hidden in the data below, but we could not tease out a statistically significant correlation. 
	Lawn: Counter({u'': 232, u'United States': 13, u'Canada': 9, u'New York, USA': 8, u'Connecticut, USA': 5, u'California, USA': 4, u'Denver, CO': 4, u'Minnesota, USA': 4, u'Florida, USA': 4, u'Ohio': 3, u'Indianapolis, IN': 3, u'Pittsburgh, PA': 3, u'Manchester': 3, u'Ontario, Canada': 3, u'Omaha, NE': 3, u'England, United Kingdom': 3, u'Ohio, USA': 3, u'Columbus, OH': 3, u'Pennsylvania, USA': 3, u'St Paul, MN': 2, u'Seattle': 2, u'Yardley, PA': 2, u'Tennessee, USA': 2, u'Portland, OR': 2, u'Italy': 2, u'Alaska, USA': 2, u'Cincinnati, OH': 2, u'Los Angeles, CA': 2, u'London, England': 2, u'Chicago, IL': 2, u'Tulsa, OK': 2, u'Kansas City, MO': 2, u'New Jersey, USA': 2, u'Detroit, MI': 2, u'Michigan, USA': 2, u'Dallas, TX': 2, u'New York': 2, u'Virginia, USA': 2, u'Nashville, TN': 2, u'Wisconsin': 2, u'Fargo, ND': 2, u'Orlando, FL': 2, u'Maryland, USA': 2, u'Washington, USA': 2, u'Arkansas, USA': 2, u'Washington, DC': 2, u'Iowa': 2, u'Buffalo, NY': 2, u'Norman, OK': 2, u'New Mexico': 2, u'Ireland': 2, u'California': 2, u'Cleveland': 2, u'Charlotte, NC': 2, u'Sydney, New South Wales': 2, u'Austin, TX': 2, u'United Kingdom': 2, u'Atlanta, Ga': 2, u'Arizona, USA': 2, u'Australia': 2, u'Brooklyn, NY': 2, u'NJ': 2, u'Providence, RI': 2, u'Morgantown, WV': 2, u'Georgia, USA': 2, u'Alberta, Canada': 2, u'Richmond, VA': 2, u'Unceded Coast Sailish Terr.': 1, u'In your musical dreams.': 1, u'Austin, Texas, USA': 1, u'EnergyDrinks': 1, u'my house': 1, u'Indiana': 1, u'Bend, OR, USA': 1, u'The Brume, Ishgard (eos / aether)': 1, u'\\_(\u30c4)_/': 1, u'Purgatory': 1, u'Abukkake': 1, u'Illinois, chicagoland': 1, u'Golden Corral': 1, u'Atlanta': 1, u'Quad Cities': 1, u'Looking for the Truth': 1, u'Celestial': 1, u'Machesney Park, IL Rockford,IL': 1, u'Morristown': 1, u'Abington PA.': 1, u'Nottingham \U0001f1ec\U0001f1e7\U0001f1ea\U0001f1fa': 1, u'Kingston, ON ': 1, u'Milton Keynes ': 1, u'chesapeake, va': 1, u'La Plata, MD': 1, u'Twitch.tv/cvst': 1, u'9 1 2': 1, u'Swindon, England': 1, u'NY. LA. ': 1, u'Towson, MD': 1, u'the dumpster': 1, u'Lancashire UK ': 1, u'Somerset': 1, u'I freaked it': 1, u'Nevada, MO': 1, u'Haldimand County, Ontario': 1, u'chicago': 1, u'Vale of Pewsey': 1, u'America': 1, u'Olathe ks': 1, u'Olathe, KS': 1, u'Litchfield, CT': 1, u'Orangeville, UT': 1, u'Flipadelphia': 1, u'Pacific Northwest': 1, u'Louisville Kentucky': 1, u'Henley-on-Thames, England': 1, u'Lansing, MI': 1, u'Northern Illinois': 1, u'Baltimore, MD &Deland Floirda ': 1, u'Central Cali Valley': 1, u'Gause, Texas': 1, u'Michigan \U0001f332\U0001f34e\U0001f33d\U0001f352\U0001f698': 1, u"near Greg's place": 1, u'Kansas City, Missouri': 1, u'Prestwood, Bucks, UK': 1, u'SW Michigan': 1, u'1.8.19': 1, u'Portland, Maine': 1, u'Indianapolis': 1, u'Rural Utah': 1, u'Troy, MI': 1, u'I am all around you.': 1, u'St. Louis, Missouri': 1, u'Malone, NY': 1, u'San Francisco, CA': 1, u'pride: paddys pub': 1, u'Alva, Scotland': 1, u'Philadelphia, PA': 1, u'Pretty far out there': 1, u'The middle, Englandcestershire': 1, u'Goleta, CA': 1, u'maryland': 1, u'Stoughton, WI': 1, u'Meadow Lakes, Ak': 1, u'Tyler, TX': 1, u'Layton, UT': 1, u'Escondido, California. 92026': 1, u'birmingham uk': 1, u'Dubuque, IA': 1, u'Edmonton, AB': 1, u'Bradford, Pa': 1, u'snapchat seekei ': 1, u'1.6.8.5': 1, u'Washington DC': 1, u'The Planet of Brooklyn': 1, u'The Republic of Texas': 1, u'East Side of Compton ': 1, u'here & there ': 1, u'VA / \U0001f1ec\U0001f1f9': 1, u'Portland Oregon': 1, u'PIT-JERU-NYC-CLE': 1, u'England ': 1, u'On tour. No sleep \u2018til Valhall': 1, u'Dublin': 1, u'Holmen, WI': 1, u'Southern New Hampshire USA': 1, u"Gorgeous Prince George's": 1, u'US Army \U0001f1fa\U0001f1f8 | @Peyak_': 1, u'Gresham, OR': 1, u'men need love too\U0001f5e3': 1, u'Cape Cod, MA': 1, u'Wareham, MA': 1, u'right behind you!': 1, u'Tampa, FL': 1, u'South Cambridgeshire, UK': 1, u'S.E. Concord Twp near Hambden': 1, u'Incline Village, Lake Taheezi': 1, u'Appalachia': 1, u'Bellevue, WA': 1, u'Sioux Falls, SD': 1, u'hell': 1, u'Texas': 1, u'Callicoon, NY': 1, u'Alexandria, VA': 1, u'Estados Unitos': 1, u'conneaut arts center yo': 1, u'Seattle, WA': 1, u'Birmingham .': 1, u'Here': 1, u'Labrador, Eastern Canada': 1, u'spartan // ms': 1, u'Indiana, USA': 1, u'Robbinsdale, MN': 1, u'Confederate flag across the st': 1, u'Delaware, USA': 1, u'Iowa, USA': 1, u'Lexington via Prestonsburg': 1, u'Sumerduck, VA': 1, u"Don't make me come over there.": 1, u'Norwich, England': 1, u'The Mitten': 1, u'raving about "halo" by MONO': 1, u'Valley of the Shadow of Death': 1, u'The TARDIS': 1, u'New Jersey': 1, u'near washington dc': 1, u'Bloomington, MN': 1, u'Iowa City, IA': 1, u'Houston, TX': 1, u'Springfield, IL': 1, u'w/ meghan probably': 1, u'its ok, youre ok': 1, u'Leeds, West Yorkshire, England': 1, u'Grand Rapids, MI': 1, u'Michigan': 1, u'Grayson, GA': 1, u'38\xb053\u203251.61\u2033N 77\xb02\u203211.58\u2033W': 1, u'im here': 1, u'Everywhere': 1, u'Wenatchee, WA': 1, u'Down South, UK': 1, u'Yorkville, Illinois': 1, u'Miami, FL': 1, u'410': 1, u'Thunder Dome': 1, u'Edmonton, Alberta, Canada': 1, u'Iowa City': 1, u'mel, aus': 1, u'the twilight zone': 1, u'Dublin, Ireland': 1, u'West Virginia, USA': 1, u'North Saint Paul , Minnesota .': 1, u'waterloo': 1, u'South Africa': 1, u'Boston': 1, u'San Diego, CA': 1, u'Massachusetts, USA': 1, u'\U0001d4ab\U0001d4c1\U0001d4b6\U0001d4c3\U0001d452\U0001d4c9 \U0001d438\U0001d4b6\U0001d4c7\U0001d4c9\U0001d4bd': 1, u'Oxfordshire': 1, u'Santa Monica': 1, u'Massachusetts and Abaln\u0101s': 1, u'Urbandale, IA': 1, u'outer space \U0001f6f8': 1, u'\u2764\ufe0fHere, There, Nowhere \u2764\ufe0f': 1, u'hopefully in the bed': 1, u'Kalamazoo, MI': 1, u'Swaggerville': 1, u'Edgar, WI': 1, u'Beautiful Toronto': 1, u'North Richland Hills Tx': 1, u'Belgium': 1, u'Ann Arbor, Michigan': 1, u'Victor, New York': 1, u'Wichita, KS': 1, u'PDX': 1, u'pittsburgh': 1, u'Baton Rouge, LA': 1, u'Southern Wisconsin': 1, u'\U0001d68d\U0001d68a\U0001d697\U0001d692': 1, u'Little China ': 1, u'Colorado, USA': 1, u'toronto': 1, u'815': 1, u'KS': 1, u'nermins heart': 1, u'Arlington, TX': 1, u'Winston Salem, NC': 1, u'Pontiac, MI': 1, u'Mostly on the ground ': 1, u'This is fine': 1, u'Orbiting your planet.': 1, u'Chilladelphia': 1, u'Lawrence, KS': 1, u'philly': 1, u'North West, England': 1, u'Port Huron, MI': 1, u'Minneapolis, MN': 1, u'Olympia, WA': 1, u'Salt Lake City, UT': 1, u'Long Island, NY': 1, u'South Lebanon, OH': 1, u'Moscow, ID': 1, u'Edmonton, Alberta': 1, u'Dixie, Washington': 1, u'Sarasota, FL': 1, u'Bartlett, IL': 1, u'Clawson, MI': 1, u'The Cotswolds UK': 1, u'Not in Kansas Anymore': 1, u'New Hampshire, USA': 1, u'Lebanon Missouri': 1, u'Earth': 1, u'Discovery Bay, Ca': 1, u'Zanesville, OH': 1, u'Western New York': 1, u'WA': 1, u'Head Lights': 1, u'Twin Cities': 1, u'Alnwick, Northumberland': 1, u'Expats in Penntucky': 1, u'Upstate New York': 1, u'Everfree Castle, Equestria': 1, u'Minerva, OH': 1, u'Idaho, USA': 1, u'Niagara Falls, NY': 1, u'Yorkshire, The North.': 1, u'Itasca County, Minnesota': 1, u'minnesota': 1, u'Crawley, West Sussex': 1, u'Canada \U0001f341': 1, u'#SaveODAAT': 1, u'Barnegat, NJ 08005': 1, u'northern NY': 1, u'Ames, IA': 1, u'The Hawkeye State': 1, u'michigan': 1, u'Dublin City, Ireland': 1, u'The Middle Coast - Oklahoma.': 1, u'Innabag': 1, u'Boca Raton, Florida': 1, u'County of Lake in da ILL state': 1, u"i've bin every where man..!!! ": 1, u'Hell': 1, u'Afghanistan': 1, u'South Carolina.': 1, u'Leeds/York, Yorkshire': 1, u'ryan@dondivamag.com': 1, u'Ohio, Earth': 1, u'Kansas City, Mo.': 1, u'Dublin Ireland': 1, u'kansas.': 1, u'France': 1, u'Downtown, Connecticut': 1, u'Track House, Atlanta': 1, u'Dangerous Territory': 1, u'Bury, England': 1, u'The Call of the Mountains': 1, u'LAvon, USA': 1, u'Leeds': 1, u'WNY': 1, u'Mountain Rock, Idaho': 1, u'Dearborn, MI': 1, u'Florida': 1, u'Witney': 1, u'DeLand, FL': 1, u'Louisiana, USA': 1, u'NoVA': 1, u'NE Ohio. Near Lake Erie.': 1, u'White Cloud, Michigan': 1, u'Sheridan, WY, United States': 1, u'Savannah, GA': 1, u"nasty 'nati": 1, u'Manhattan, KS': 1, u'Piedmont, OK': 1, u'sort of west of london': 1, u'Scotland.': 1, u'15 Yemen Rd, Yemen': 1, u'In a strip club at Mos Eisley': 1, u'Wilmington, NC': 1, u'jungoogs right nipple hole': 1, u'The Woods, CT': 1, u'USA': 1, u'609 to 410': 1, u"Can't figure it out?": 1, u'Queensland': 1, u'ontario :)': 1, u' Bay Area, Ca. \U0001f31e': 1, u'Toronto': 1, u'Georgia': 1, u'Duval FL, USA (Memphis, TN)': 1, u'Aurora, IL': 1, u'San Jose, CA': 1, u'Pennsylvania': 1, u'Dagobah': 1, u'Cheektowaga NY USA ': 1, u'DSGG': 1, u'DC': 1, u'BC, Canada': 1, u'La Crosse, Wisconsin': 1, u'StL by way of KC, South Canada': 1, u'Davenport': 1, u'Fenton, MI': 1, u'Southern Oregon': 1, u'Lives near Port Stanley ON': 1, u'Queensland, Australia': 1, u'Chicagoland': 1, u'nku \u201821': 1, u'Cleveland, GA': 1, u'New York, NY': 1, u'Dayton, OH': 1, u'Town of Myst': 1, u'Buffalo NY': 1, u'Northeast Ohio': 1, u'Glen Ellyn, IL': 1, u'lawrence ks ': 1, u'Scandinavia': 1, u'Wisconsin, USA': 1, u'Baltimore, MD': 1, u'U.S. of  A.': 1, u'Nashville': 1, u'CANADA BABY \U0001f1e8\U0001f1e6': 1, u'trudeauistan': 1, u'New Hampshire': 1, u'Hillsboro, Oregon': 1, u'Eating ': 1, u'WoW, Fallout, Metro, indy. ': 1, u'Eugene, OR': 1, u'KCMO': 1, u'The gym': 1, u'\xdcT: 42.523846,-70.90242': 1, u'Emlanjeni': 1, u'Haddonfield, IL.': 1, u'Illinois, USA': 1, u'Right Here': 1, u'Elkhart, IN': 1, u'Bourbonnais, IL': 1, u"Where'z tha foadiez?": 1, u'Twilight Town': 1, u'Des Moines': 1, u'Washington Court House, OH': 1, u'Scotia, NY United States': 1, u'BGKY, by way of Detroit': 1, u'Winterfell, Westeros': 1, u'Milwaukee, WI': 1, u'Rock Island, IL': 1, u'Internet': 1, u'Saskatchewan, Canada': 1, u'Wherever I am Needed': 1, u'221B Baker St.': 1, u'L.A.,Calif/Las Vegas Nv USA': 1, u'tip toeing in my Jordans': 1, u'Illinois/Georgia, USA': 1, u'jackpot loves yo': 1, u'Atlanta, GA': 1, u'the south': 1, u'Melting in Wisconsin': 1, u'South Central Pennsylvania': 1, u'Eagle County, CO': 1, u'Kidderminster, England': 1, u'Cincinnati': 1, u'New Zealand': 1, u'Probably with dalton ': 1, u'in my house': 1, u'Dry Atlantic, Earth': 1, u'107+111+GFG+CFC': 1, u'farmingdale': 1, u'Salt Lake': 1, u'i dont know?????': 1, u"behind you, don't look!": 1, u'Orcas   ': 1, u'Central WI': 1, u'Geneva, IL': 1, u'Northern Indiana': 1, u'Saint Louis, MO': 1, u'Lancaster,Missouri': 1, u'peace.': 1, u'Bay Area': 1, u'Central Wisconsin': 1, u'Over here': 1, u'Delmar N.Y': 1, u'Living in Reality, North America': 1, u'Polska': 1, u'Boston, MA': 1, u'Kentucky, USA': 1, u'The tweets are coming from inside the house.': 1, u'iPhone: 0.000000,0.000000': 1, u'Flyover country, Iowa': 1, u'New Orleans, LA': 1, u'Centre, France': 1, u'Flint, MI - USA': 1, u'Dahlonega, Georgia': 1, u'Where the stars are bright... ': 1, u'UK': 1, u'Birmingham, AL': 1, u'gin shae rae noora mavi alexa': 1, u'Cedar Falls, IA': 1, u'Philadelphia, Pa,, USA': 1, u'Coquitlam, British Columbia': 1, u'Colorado Springs, CO': 1, u'My Twitch (Weeb Cringe)~\U0001f495 \u23ec': 1, u'webberville mi': 1, u'Brockport, NY': 1, u'Woodstock': 1, u'Arkansas': 1, u'a desk near a window': 1, u'NC - NJ - PA': 1, u'New York ': 1, u'814 via 215': 1, u'Durham, NC': 1, u'Fond du Lac, WI': 1, u'Somewhere in the Clouds': 1, u'Maine, USA': 1, u'Chanute,KS': 1, u'pa': 1, u'Morrisville, NC, USA': 1, u'Tulsa, Oklahoma': 1, u'Shut up': 1, u'757': 1, u'South West, England': 1, u'Ludlow, KY': 1, u'Warden , usa': 1, u'Kalamazoo, Michigan (The Hand)': 1, u'Asbury Park, NJ': 1, u'tiredsleep@hotmail.com': 1, u'Hertfordshire, UK ': 1, u'Mount Pleasant, MI': 1, u'alberta, canada': 1, u'Chicago,IL': 1, u'Moonpar Australia': 1, u'Twitter': 1, u'Norman/Lawton, Oklahoma': 1, u'I Would Die For Professor McGonagall\u2122\ufe0f': 1, u'Cambridge, England': 1, u'Ann Arbor, MI': 1, u'Cleveland, OH': 1, u'Higham Ferrers, England': 1, u'White Sands': 1, u'Madison, WI': 1, u'Newport, S Wales': 1, u'Second Life and San Antonio TX': 1, u'Hampton Court': 1, u'White Lake, MI': 1, u'Sylacauga, AL': 1, u'Texas, USA': 1, u'Tarrant County, TX': 1, u'Waterford, MI': 1, u'Massillon, OH x Biloxi, MS ': 1, u'Bolton Point': 1, u'they/them': 1, u'Utah': 1, u'San Marcos, TX': 1, u'Las Vegas, NV': 1, u'looking at a screen, somewhere': 1, u'Red Bank, NJ': 1, u'North Idaho': 1, u'\U0001f414 ': 1, u'World Wide.': 1, u'screwston, TX': 1, u'Istanbul, Turkey': 1, u'Ottawa or NWR': 1, u'Cambridge Ontario': 1, u'northbridge': 1, u'Norfolk, NE': 1, u'David Bowie Is A Pediphile ': 1, u'Marietta, GA': 1, u'Stoke-on-Trent, England': 1, u'Mifflintown, PA': 1, u'Canton, GA': 1, u'Smack Dab in the Middle': 1, u'South Dakota, USA': 1, u'illiNoise': 1})
	Whiteboard: Counter({u'New York, NY': 63, u'Brooklyn, NY': 43, u'': 32, u'New York City': 30, u'NYC': 29, u'New York': 18, u'New York, USA': 15, u'Manhattan, NY': 10, u'San Francisco, CA': 7, u'Los Angeles, CA': 6, u'San Francisco': 4, u'New York, NY, USA': 4, u'Hoboken, NJ': 4, u'Washington, DC': 3, u'Brooklyn, New York': 3, u'Boston, MA': 3, u'United States': 3, u'nyc': 3, u'BK': 2, u'Long Island City, Queens': 2, u'Brooklyn': 2, u'Jersey City, NJ': 2, u'NY, NY': 2, u'Sydney, New South Wales': 2, u'Austin, TX': 2, u'Denver, CO': 2, u'Newark': 1, u'Battery Park City, NYC': 1, u'Port Washington NY': 1, u'Upstate New York': 1, u'Brooklyn, ny': 1, u'iPhone: 40.797558,-73.957237': 1, u'Bronx, NY': 1, u'Woodside, NY': 1, u'Berlin \u2022 he/him/his': 1, u'Fairfield & Hoboken NJ': 1, u'\xdcT: 40.742661,-73.983157': 1, u'Jamaica': 1, u'new york city': 1, u'Dublin City, Ireland': 1, u'NYC/DMV/SPAIN/AFRICA/JAPAN': 1, u'Virginia Beach, VA': 1, u'Bloomfield NJ': 1, u'Valley Stream, NY': 1, u'Jersey City, New Jersey': 1, u'\xdcT: 40.808222,-73.962212': 1, u'brooklyn ny': 1, u'Astoria, NYC': 1, u'no longer jc, but still nj': 1, u'Newark, NJ ': 1, u'New Jersey': 1, u'Gotham': 1, u'NJ/Hudson County/Absurdistan': 1, u'new york city -ish': 1, u'Milano, Italy': 1, u'east village': 1, u'philly / nyc': 1, u'Houston, TX': 1, u'LI - NYC ': 1, u'Mission, San Francisco': 1, u'East Village, NY': 1, u'Brooklyn - Palo Alto': 1, u'Currently, Earth': 1, u'Dumont, New Jersey': 1, u'NYC, NY ': 1, u'Fairfield, Conn.': 1, u'Peterborough, NH': 1, u'Paris, France': 1, u'Queens, NY': 1, u'Bay Area': 1, u'IBA, NYU | New York City': 1, u'PA': 1, u'Everywhere': 1, u'LA': 1, u'Minneapolis, MN': 1, u'new new york': 1, u'Crown Heights, Brooklyn': 1, u'North America': 1, u'Melbourne, Australia': 1, u'Barcelona': 1, u'Baltimore, MD': 1, u'SFO [next: Seoul and Da Nang]': 1, u'Deep Burbs of NYC': 1, u'Bushwick': 1, u'Decentralized': 1, u'Bayonne, NJ ': 1, u'Long Island City, NY': 1, u'd. | 04.01.16 | 03.27.18': 1, u'37\xb014\u203206\u2033N 115\xb048\u203240\u2033W': 1, u'Manhattan, NYC, NY': 1, u'| NYC + NC + LA |': 1, u'Paramus, NJ': 1, u'in the concrete jungle.': 1, u'\xdcT: 40.72383,-73.992294': 1, u'Manchester, England': 1, u'Amherst, MA': 1, u'Lincoln Financial Field': 1, u'Sweet Home Chicago': 1, u'Gilbert, AZ': 1, u'Golden Gate, San Francisco': 1, u'Portland, OR': 1, u'Leeds, England': 1, u'New York, New York': 1, u'Vero Beach, FL': 1, u'Polar vortex': 1, u'Staten Island, NY': 1, u'NJ': 1, u'NYC, SF, CHI, TO, KW, LON, PAR, SYD, DUS, LA, MI': 1, u'Union City, NJ': 1, u'USA': 1, u'San Diego, CA': 1, u'Seattle, WA +': 1, u'Time & Space': 1, u'Nashville, TN and New York, NY': 1, u'New York City, NY, USA': 1, u'nyc metro': 1, u'Lawrence, NY': 1, u'NJ/NYC': 1, u'Wheeling, WV': 1, u'\xdcT: 40.740482,-74.005944': 1, u'Tempe, AZ': 1, u'The Musecage': 1, u'Chelsea, Manhattan': 1, u'Philadelphia, PA': 1, u'Miami Beach, FL': 1, u'Louisville, KY': 1, u'\xdcT: 40.740808,-73.8951992': 1, u'48-06 41st Street, Sunnyside': 1, u'Queens Bully, NY': 1, u'Washington, D.C.': 1, u'The Emerald Cave': 1, u'Hamptons New York': 1, u'New York-ish': 1, u'NYC+SF+TDOT+LDN': 1, u'Queens, NY\u2194\ufe0fMYR': 1, u'SF': 1, u'Salt Lake City / Brooklyn': 1, u'Woodruff, Utah, USA': 1, u'Elmhurst NY': 1, u'Nightmare Realm / Moonville': 1, u'Santa Monica, CA': 1, u'NJ/FL/NYC': 1, u'Santa Fe, NM': 1, u'Brooklyn via Bangalore': 1, u'Dumont, NJ': 1, u'honeymoon \xe3ve': 1, u'Crown Heights': 1, u'what is, new york city': 1, u'IG:@MHSexpert': 1, u'Bayside,  Queens': 1, u'Las Vegas, NV': 1, u'Wildwood, NJ': 1, u'Uptown & The Bronx': 1, u'NYC Sprawl': 1, u'Williamsburg, Brooklyn - NYC': 1, u'NJ, USA': 1, u'brooklyn': 1, u'Big Apple': 1, u'iPhone: 33.801552,-117.921272': 1, u'HERE I AM': 1, u'Dontt worryy boutt mee ': 1, u'Chicago, IL': 1, u'NEW YORK CITY': 1, u'Singapore': 1, u'NYC / IG: @a0k': 1, u'Long Island': 1, u'\xdcT: 40.8264932,-73.8570042': 1, u'new york city baby': 1, u'Brooklyn, USA': 1})
	Trolls: Counter({u'': 36, u'United States': 9, u'USA': 6, u'Texas, USA': 3, u'Ohio, USA': 3, u'California, USA': 2, u'Arizona, USA': 2, u'Florida, USA': 2, u'New York, USA': 2, u'SomeWhere Over The Rainbow !! ': 1, u'Live Free or Die, USA': 1, u'South Carolina, USA': 1, u'\U0001f1fa\U0001f1f8\U0001f1fa\U0001f1f8\U0001f1fa\U0001f1f8\U0001f1fa\U0001f1f8\U0001f1fa\U0001f1f8\U0001f1fa\U0001f1f8\U0001f1fa\U0001f1f8': 1, u'Alcoa, TN': 1, u'Florida ': 1, u'Deploraville, USA': 1, u'Edmonton Alberta Canada. ': 1, u'Algona, IA': 1, u'Auburndale, FL': 1, u'Urbandale, IA': 1, u'Arkansas': 1, u'Michigan, USA': 1, u'Kansas, USA': 1, u'North Carolina, USA': 1, u'Vancouver, British Columbia': 1, u'Queens, NY': 1, u'Backwash of Finerio': 1, u'Washington, USA': 1, u'Maine, USA': 1, u'Largo, Florida': 1, u'La, USA': 1, u'Here': 1, u'Susanville, CA': 1, u'Pittsburgh, PA': 1, u'Huntsville, AL': 1, u'California': 1, u'Oklahoma, USA': 1, u'The Show.': 1, u'Memphis': 1, u'Followed by @PastorBobJoyce!': 1, u'Lawndale Ca': 1, u'Georgia': 1, u'The Promised Land \u2022  \u2022\u2022  \u2022\u2022\u2022 ': 1, u'Rhode Island, USA': 1, u'Everywhere': 1, u'United States, Ohio': 1, u'Deutschland': 1, u'Ga/MS/WV': 1, u'Canada but MAGA supporter': 1, u'Michigan ': 1, u'The last FREE country on Earth.': 1, u'Missouri': 1, u'Illinois, USA': 1, u'\U0001f1fa\U0001f1f8Oklahoma\U0001f1fa\U0001f1f8': 1, u'Austin': 1, u'Norfolk, VA': 1, u'Illinois USA ': 1, u'Indiana, USA ': 1, u'Jackson, MI': 1, u'Southwest Missouri': 1, u'Clearwater, FL': 1, u'ComeGetSome, Texas \U0001f1fa\U0001f1f8': 1, u'Guam': 1, u'Chicago, IL': 1, u'CA Reagan Conservative': 1, u'Virginia, USA': 1, u'Lexington, KY': 1, u'UK': 1, u'Mansfield, Ohio': 1, u'Gilbert, AZ': 1, u'Arizona Desert': 1, u'michigander my whole life': 1, u'USA!': 1})
2. **Geo Tagged Locations**
	Twitter is deprecating this field from the Profile API, so this is becoming less relevant by the day. 
	Not an Indicator
	Lawn: Counter({None: 823, u'United States': 4, u'Denver, CO': 3, u'New York, USA': 2, u'Alaska, USA': 2, u'Tennessee, USA': 2, u'Kansas City, MO': 2, u'California, USA': 2, u'St Paul, MN': 2, u'Higham Ferrers, England': 1, u'Zanesville, OH': 1, u'Ohio, USA': 1, u'Detroit, MI': 1, u'Ireland': 1, u'Delaware, USA': 1, u'Norman, OK': 1, u'Glen Ellyn, IL': 1, u'Bellevue, WA': 1, u'Coquitlam, British Columbia': 1, u'Pennsylvania, USA': 1, u'Michigan, USA': 1, u'Indianapolis, IN': 1, u'Sydney, New South Wales': 1, u'Alexandria, VA': 1, u'Portland, OR': 1, u'San Marcos, TX': 1, u'Milwaukee, WI': 1, u'Olympia, WA': 1, u'Robbinsdale, MN': 1, u'Nashville, TN': 1, u'White Lake, MI': 1, u'Austin, TX': 1, u'Wichita, KS': 1, u'Malone, NY': 1, u'Grand Rapids, MI': 1, u'Eugene, OR': 1, u'Kentucky, USA': 1, u'Wenatchee, WA': 1, u'Dublin City, Ireland': 1, u'Idaho, USA': 1, u'London, England': 1, u'Norwich, England': 1, u'Baton Rouge, LA': 1, u'Kidderminster, England': 1, u'Omaha, NE': 1, u'Sarasota, FL': 1, u'Colorado, USA': 1, u'Illinois, USA': 1, u'South Africa': 1, u'Manhattan, KS': 1, u'Mifflintown, PA': 1, u'Connecticut, USA': 1, u'South Dakota, USA': 1, u'New York, NY': 1, u'Iowa City, IA': 1, u'Ann Arbor, MI': 1, u'Houston, TX': 1, u'Cleveland, OH': 1})
	Whiteboard: Counter({None: 392, u'New York, NY': 11, u'New York, USA': 11, u'Brooklyn, NY': 5, u'Manhattan, NY': 2, u'United States': 2, u'Golden Gate, San Francisco': 1, u'Virginia Beach, VA': 1, u'Vero Beach, FL': 1, u'Paris, France': 1, u'Sydney, New South Wales': 1, u'Minneapolis, MN': 1, u'Tempe, AZ': 1, u'Los Angeles, CA': 1, u'Wildwood, NJ': 1, u'Austin, TX': 1, u'Boston, MA': 1, u'San Francisco, CA': 1, u'Crown Heights, Brooklyn': 1, u'Denver, CO': 1, u'Portland, OR': 1, u'Amherst, MA': 1})
	Trolls: Counter({None: 114, u'United States': 4, u'California, USA': 1, u'Jackson, MI': 1, u'Chicago, IL': 1, u'Arizona, USA': 1, u'Texas, USA': 1, u'Algona, IA': 1, u'Auburndale, FL': 1, u'Pittsburgh, PA': 1, u'Florida, USA': 1, u'Oklahoma, USA': 1, u'Guam': 1})
3. Number of Lists a Member is Added To
	No statistical correlation between the number of lists Suspected Propagandists are members of versus normal accounts. 
	Not an Indicator
	Lawn: AVERAGE: 25.76206509539843, MEDIAN: 3.0, 10: 0.0, 90: 49.0, stddev: 126.82161158398418
	Whiteboard: AVERAGE: 154.36446469248293, MEDIAN: 33.0, 10: 2.0, 90: 361.3999999999999, stddev: 429.89012657193007
	Trolls: AVERAGE: 28.906976744186046, MEDIAN: 4.0, 10: 0.0, 90: 71.60000000000001, stddev: 102.04782598632046
4. User Has Default Profile Image
	Also surprising, but having a default egg profile image had no correlation to being a propaganda account. There may be some value in doing object recognition or storing image metadata to ascertain whether the image is known propaganda or contains certain objects/elements. 
	Not an Indicator
	Lawn: Counter({False: 886, True: 5})
	Whiteboard: 100% False
	Trolls: 1 True
5. Sidebar Profile Color
	We tested everything, but there was no correlation between Propagandists and normal users in what color sidebar they chose. 
	Not an Indicator, despite trolls using less color variations
	Lawn: Counter({u'DDEEF6': 449, u'000000': 208, u'252429': 28, u'EFEFEF': 26, u'C0DFEC': 13, u'95E8EC': 11, u'FFFFFF': 10, u'7AC3EE': 9, u'F6F6F6': 9, u'99CC33': 8, u'DAECF4': 7, u'DDFFCC': 7, u'E6F6F9': 6, u'F6FFD1': 6, u'F3F3F3': 4, u'E5507E': 4, u'78C0A8': 4, u'C9C9C9': 3, u'E3E2DE': 2, u'FFF7CC': 2, u'A0C5C7': 2, u'1C1C1C': 2, u'C5B20D': 1, u'5E91A6': 1, u'07042A': 1, u'B0B99C': 1, u'CDB87F': 1, u'949494': 1, u'040102': 1, u'EFCEDE': 1, u'DAF0D3': 1, u'080808': 1, u'557605': 1, u'B8A2C3': 1, u'171106': 1, u'291C0D': 1, u'D8A636': 1, u'B3C8DD': 1, u'D1D1D1': 1, u'C000F0': 1, u'FBEFBF': 1, u'00A2FF': 1, u'FFC8DA': 1, u'474447': 1, u'FB6559': 1, u'E7E9F5': 1, u'FD8024': 1, u'030516': 1, u'065285': 1, u'2D182C': 1, u'BABABA': 1, u'808080': 1, u'061127': 1, u'140D14': 1, u'C7C5BD': 1, u'FFFCBD': 1, u'FCFC60': 1, u'044729': 1, u'141114': 1, u'8ACC33': 1, u'141112': 1, u'0D0D0D': 1, u'EBEBEB': 1, u'FA8A00': 1, u'D01157': 1, u'D6D6D6': 1, u'5B5E55': 1, u'F5A293': 1, u'1EEBC9': 1, u'E82351': 1, u'E69F9E': 1, u'28000F': 1, u'D9DBE0': 1, u'F25D5E': 1, u'E8E8E1': 1, u'1D231B': 1, u'E0FF92': 1, u'0E0E0E': 1, u'657D14': 1, u'020812': 1, u'CC0000': 1, u'51377A': 1, u'FAF5FA': 1, u'FCFAC9': 1, u'EBB281': 1, u'FFD505': 1, u'ACB9B5': 1, u'182A23': 1, u'63E0F0': 1, u'CCD3E7': 1, u'FFF7FF': 1, u'D2E3CA': 1, u'704B37': 1})
	Whiteboard: Counter({u'DDEEF6': 120, u'000000': 70, u'EFEFEF': 31, u'252429': 25, u'FFFFFF': 18, u'C0DFEC': 17, u'DDFFCC': 9, u'F6F6F6': 8, u'99CC33': 8, u'DAECF4': 7, u'A0C5C7': 7, u'95E8EC': 7, u'E6F6F9': 6, u'E3E2DE': 5, u'EADEAA': 4, u'F3F3F3': 4, u'E0FF92': 4, u'7AC3EE': 3, u'20201E': 3, u'F6FFD1': 3, u'FFF7CC': 2, u'061127': 2, u'333333': 2, u'20252C': 1, u'121212': 1, u'BFBFBF': 1, u'242424': 1, u'140E0A': 1, u'CDEDF7': 1, u'F7F7F7': 1, u'360000': 1, u'CCBF82': 1, u'1F1F1F': 1, u'DCE2E4': 1, u'A9B1C7': 1, u'9D989E': 1, u'CA6F3B': 1, u'CE1AA5': 1, u'14635F': 1, u'CCE4FF': 1, u'ABE0FC': 1, u'262626': 1, u'4CC5E6': 1, u'C4D49D': 1, u'142200': 1, u'FDF8E2': 1, u'F1F2F2': 1, u'A0C7C5': 1, u'FAFAFA': 1, u'C7BFBF': 1, u'EFF09E': 1, u'766B5D': 1, u'ABC9BE': 1, u'EEEDF2': 1, u'E08E14': 1, u'546D68': 1, u'858585': 1, u'9E989E': 1, u'DBDBDB': 1, u'F7E6ED': 1, u'FFF200': 1, u'8C8F72': 1, u'FFFFBB': 1, u'999999': 1, u'EDEDED': 1, u'EBEEF0': 1, u'307501': 1, u'EEE8D5': 1, u'DFEAFF': 1, u'FCF4F4': 1, u'1566C2': 1, u'99C28A': 1, u'D6D6D6': 1, u'212121': 1, u'A0E0FF': 1, u'E5507E': 1, u'D8D8D8': 1, u'E6E2DF': 1, u'E3E319': 1, u'1B9988': 1, u'AF4215': 1, u'C9CDCF': 1, u'E7EBEE': 1, u'7AABDC': 1, u'91FFA2': 1, u'020812': 1, u'0C3F3D': 1, u'702BA8': 1, u'EDFEFF': 1, u'63B4EB': 1, u'84A2F0': 1, u'CDF1FA': 1, u'E0E0E0': 1, u'B8B8B8': 1, u'1255FF': 1, u'78CBFF': 1, u'525252': 1})
	Trolls: Counter({u'DDEEF6': 91, u'000000': 26, u'DDFFCC': 4, u'95E8EC': 2, u'E5507E': 2, u'F3F3F3': 1, u'E6DA98': 1, u'F6F6F6': 1, u'FF7D5C': 1})
6. Background Profile Color
	Also no correlation between background color of the Twitter profile and spreading Propaganda. 
	Not an indicator
	Lawn: Counter({u'C0DEED': 399, u'000000': 252, u'FFFFFF': 92, u'EEEEEE': 29, u'181A1E': 22, u'A8C7F7': 11, u'BDDCAD': 7, u'5ED4DC': 7, u'C6E2EE': 6, u'829D5E': 6, u'65B0DA': 6, u'CC3366': 5, u'F0A830': 3, u'DFDFDF': 3, u'FFF8AD': 3, u'D3D2CF': 2, u'C2BEBE': 1, u'ED4C82': 1, u'9DA593': 1, u'BFBFBF': 1, u'86991D': 1, u'000515': 1, u'2280A9': 1, u'FAFAFA': 1, u'FF0000': 1, u'C6C6D1': 1, u'F2E195': 1, u'E66B00': 1, u'86A4A6': 1, u'FF9742': 1, u'FED6D6': 1, u'A71F5A': 1, u'DE4823': 1, u'DBE9ED': 1, u'07080A': 1, u'3F8A4E': 1, u'F59B75': 1, u'0A0A0A': 1, u'5B3C19': 1, u'90AFB2': 1, u'390A5C': 1, u'68FE48': 1, u'F213E3': 1, u'ED5300': 1, u'083F8C': 1, u'11EBB4': 1, u'CCD3E7': 1, u'16818E': 1, u'BACEC5': 1, u'C0DCF1': 1, u'87BC44': 1, u'B5B5B5': 1, u'E1EDCE': 1, u'3131F1': 1})
	Whiteboard: Counter({u'FFFFFF': 104, u'000000': 103, u'C0DEED': 100, u'EEEEEE': 20, u'181A1E': 16, u'A8C7F7': 10, u'BDDCAD': 7, u'829D5E': 6, u'87BC44': 6, u'86A4A6': 5, u'C6E2EE': 5, u'5ED4DC': 5, u'DBE9ED': 4, u'DFDFDF': 3, u'F2E195': 2, u'000515': 2, u'65B0DA': 2, u'C8A867': 2, u'D1D1D1': 1, u'D9B17E': 1, u'FEFCFC': 1, u'EEE8D5': 1, u'5B5B5B': 1, u'2280A9': 1, u'D3D2CF': 1, u'FF0000': 1, u'DF3F1F': 1, u'333333': 1, u'BCBEC0': 1, u'042769': 1, u'28B573': 1, u'97E265': 1, u'2F0CA3': 1, u'2A2A2A': 1, u'393E46': 1, u'636363': 1, u'8BA7C4': 1, u'CCCCCC': 1, u'EBEBEB': 1, u'DCD7C4': 1, u'C7CBD1': 1, u'F4FF00': 1, u'24DAF2': 1, u'CC3366': 1, u'3D87D7': 1, u'03060B': 1, u'F70000': 1, u'381600': 1, u'F7E6ED': 1, u'F7931E': 1, u'999999': 1, u'FAF4B9': 1, u'F9B6AD': 1, u'5C5C5C': 1, u'8494A1': 1})
	Trolls: Counter({u'C0DEED': 89, u'000000': 28, u'BDDCAD': 4, u'5ED4DC': 2, u'CC3366': 2, u'524500': 1, u'595959': 1, u'EEEEEE': 1, u'DFDFDF': 1})
