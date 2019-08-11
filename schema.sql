--
-- PostgreSQL database dump
--

-- Dumped from database version 11.2
-- Dumped by pg_dump version 11.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: prop; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE prop WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


\connect prop

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: fail_queue; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.fail_queue (
    username text NOT NULL,
    error text
);


--
-- Name: hashtags; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.hashtags (
    hashtagid integer NOT NULL,
    hashtag_user text,
    hashtag text,
    "timestamp" timestamp without time zone,
    tweet_id text NOT NULL
);


--
-- Name: hashtags_hashtagid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.hashtags_hashtagid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: hashtags_hashtagid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.hashtags_hashtagid_seq OWNED BY public.hashtags.hashtagid;


--
-- Name: ioc_domains; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ioc_domains (
    ioc_id integer NOT NULL,
    ioc_domain text NOT NULL,
    ioc_weight integer,
    ioc_classification text
);


--
-- Name: ioc_domains_ioc_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ioc_domains_ioc_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ioc_domains_ioc_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ioc_domains_ioc_id_seq OWNED BY public.ioc_domains.ioc_id;


--
-- Name: ioc_hashtags; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ioc_hashtags (
    ioc_id integer NOT NULL,
    ioc_hashtag text,
    ioc_weight integer,
    ioc_classification text
);


--
-- Name: ioc_hashtags_ioc_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ioc_hashtags_ioc_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ioc_hashtags_ioc_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ioc_hashtags_ioc_id_seq OWNED BY public.ioc_hashtags.ioc_id;


--
-- Name: ioc_urls; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ioc_urls (
    ioc_id integer NOT NULL,
    ioc_url text NOT NULL,
    ioc_weight integer,
    ioc_classification text
);


--
-- Name: ioc_urls_ioc_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ioc_urls_ioc_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ioc_urls_ioc_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ioc_urls_ioc_id_seq OWNED BY public.ioc_urls.ioc_id;


--
-- Name: links; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.links (
    linkid integer NOT NULL,
    link_user text,
    link_url text,
    link_domain text,
    "timestamp" timestamp without time zone,
    tweet_id text NOT NULL
);


--
-- Name: links_linkid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.links_linkid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: links_linkid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.links_linkid_seq OWNED BY public.links.linkid;


--
-- Name: queue; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.queue (
    username text NOT NULL
);


--
-- Name: retweeted_users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.retweeted_users (
    retweetid integer NOT NULL,
    retweeted_user text,
    "timestamp" timestamp without time zone,
    score integer,
    tweet_id text,
    username text
);


--
-- Name: retweeted_users_retweetid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.retweeted_users_retweetid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: retweeted_users_retweetid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.retweeted_users_retweetid_seq OWNED BY public.retweeted_users.retweetid;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    username text NOT NULL,
    followers integer,
    followers_per_day numeric,
    following integer,
    following_per_day numeric,
    days_since_joining numeric,
    num_of_tweets integer,
    tweets_per_day numeric,
    likes integer,
    likes_per_day numeric,
    hashtag_desc boolean,
    emoji_name boolean,
    emoji_double boolean,
    emojihash_triple boolean,
    geo_extended boolean,
    bhash_count integer,
    has_profile_url boolean,
    profile_url text,
    account_score integer,
    account_score_bhash integer,
    account_score_tweets integer,
    account_score_following integer,
    account_score_follower integer,
    account_score_likes integer,
    verified boolean,
    last_scrape timestamp without time zone,
    content_score integer,
    all_iocs text,
    general_conspiracy integer,
    radical_conspiracy integer,
    right_social_issues integer,
    right_media integer,
    alt_right_media integer,
    malicious_media integer,
    russian_media integer,
    radical_platform_migration integer,
    christian_right integer,
    usa_race_relations integer,
    defend_mike_flynn integer,
    left_voter_suppression integer,
    discredit_left integer,
    right_voter_encouragement integer,
    promote_trump integer,
    attack_trump integer,
    support_republican_campaign integer,
    discredit_media integer,
    propagandist_tools integer,
    brexit integer,
    venezuela_influence integer,
    democrat_nonspecific integer,
    canada_influence integer,
    usa_influence_nonspecific integer,
    australia_influence integer,
    malicious_monetization integer,
    discredit_usa_institutions integer,
    primary_class text,
    europe_influence integer,
    appears_automated boolean,
    status text,
    geo_city text,
    geo_state text,
    geo_country text
);


--
-- Name: hashtags hashtagid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.hashtags ALTER COLUMN hashtagid SET DEFAULT nextval('public.hashtags_hashtagid_seq'::regclass);


--
-- Name: ioc_domains ioc_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ioc_domains ALTER COLUMN ioc_id SET DEFAULT nextval('public.ioc_domains_ioc_id_seq'::regclass);


--
-- Name: ioc_hashtags ioc_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ioc_hashtags ALTER COLUMN ioc_id SET DEFAULT nextval('public.ioc_hashtags_ioc_id_seq'::regclass);


--
-- Name: ioc_urls ioc_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ioc_urls ALTER COLUMN ioc_id SET DEFAULT nextval('public.ioc_urls_ioc_id_seq'::regclass);


--
-- Name: links linkid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.links ALTER COLUMN linkid SET DEFAULT nextval('public.links_linkid_seq'::regclass);


--
-- Name: retweeted_users retweetid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.retweeted_users ALTER COLUMN retweetid SET DEFAULT nextval('public.retweeted_users_retweetid_seq'::regclass);


--
-- Name: fail_queue fail_queue_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.fail_queue
    ADD CONSTRAINT fail_queue_pkey PRIMARY KEY (username);


--
-- Name: users fetched_users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT fetched_users_pkey PRIMARY KEY (username);


--
-- Name: hashtags hashtags_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.hashtags
    ADD CONSTRAINT hashtags_pkey PRIMARY KEY (hashtagid);


--
-- Name: ioc_domains ioc_domain; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ioc_domains
    ADD CONSTRAINT ioc_domain UNIQUE (ioc_domain) INCLUDE (ioc_domain);


--
-- Name: ioc_domains ioc_domains_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ioc_domains
    ADD CONSTRAINT ioc_domains_pkey PRIMARY KEY (ioc_id);


--
-- Name: ioc_hashtags ioc_hashtag; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ioc_hashtags
    ADD CONSTRAINT ioc_hashtag UNIQUE (ioc_hashtag) INCLUDE (ioc_hashtag);


--
-- Name: ioc_hashtags ioc_hashtags_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ioc_hashtags
    ADD CONSTRAINT ioc_hashtags_pkey PRIMARY KEY (ioc_id);


--
-- Name: ioc_urls ioc_unique_url; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ioc_urls
    ADD CONSTRAINT ioc_unique_url UNIQUE (ioc_url) INCLUDE (ioc_url);


--
-- Name: ioc_urls ioc_urls_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ioc_urls
    ADD CONSTRAINT ioc_urls_pkey PRIMARY KEY (ioc_id);


--
-- Name: links links_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.links
    ADD CONSTRAINT links_pkey PRIMARY KEY (linkid);


--
-- Name: queue queue_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.queue
    ADD CONSTRAINT queue_pkey PRIMARY KEY (username);


--
-- Name: retweeted_users retweeted_users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.retweeted_users
    ADD CONSTRAINT retweeted_users_pkey PRIMARY KEY (retweetid);


--
-- Name: retweeted_users tweets; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.retweeted_users
    ADD CONSTRAINT tweets UNIQUE (tweet_id) INCLUDE (tweet_id);


--
-- Name: hashtags tweetshashes; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.hashtags
    ADD CONSTRAINT tweetshashes UNIQUE (tweet_id) INCLUDE (tweet_id);


--
-- Name: links tweetslinks; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.links
    ADD CONSTRAINT tweetslinks UNIQUE (tweet_id) INCLUDE (tweet_id);


--
-- Name: hashtags_user_index; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hashtags_user_index ON public.hashtags USING btree (hashtag_user);


--
-- Name: links_domains; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX links_domains ON public.links USING btree (link_domain);


--
-- Name: links_user_index; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX links_user_index ON public.links USING btree (link_user);


--
-- Name: user_account_score; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_account_score ON public.users USING btree (account_score);


--
-- Name: user_content_score; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_content_score ON public.users USING btree (content_score);


--
-- Name: user_score_index; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_score_index ON public.users USING btree (account_score);


--
-- Name: user_scrape; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_scrape ON public.users USING btree (last_scrape);


--
-- Name: user_scrape_index; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_scrape_index ON public.users USING btree (last_scrape);


--
-- Name: user_status; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_status ON public.users USING btree (status);


--
-- Name: user_username_index; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_username_index ON public.users USING btree (username);


--
-- PostgreSQL database dump complete
--

