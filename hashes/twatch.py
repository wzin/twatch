#!/opt/local/bin/python
#Consumer key    1ygxvqNaL4f2fOj4YI2Nnw
#Consumer secret     be9bW9PrCfPYeSlTQtHmlP3YDYv1p6frU3yE4wW3c
#Request token URL   https://api.twitter.com/oauth/request_token
#Authorize URL   https://api.twitter.com/oauth/authorize
#Access token URL    https://api.twitter.com/oauth/access_token
#Callback URL    None

import sqlite3
import twitter
import os 
import sys

try:
    sys.path.append(str(os.path.abspath(os.curdir)).replace('hashes',''))
    import hashes
except ImportError:
    print("Could not import twatch")

record = { 'status' : '',
           'id'     : '',
           'timestamp':''}



api = twitter.Api()
api = twitter.Api(consumer_key='1ygxvqNaL4f2fOj4YI2Nnw',consumer_secret='be9bW9PrCfPYeSlTQtHmlP3YDYv1p6frU3yE4wW3c', access_token_key='482945860-qF6j9CkLjaLBSVSGYkJqk2rXxHj3SO6EQrR5LP8k', access_token_secret='8hnU3r2wcLV6CcRF8lJrSAp4cdMXYH9BJqmV812Y') 
print api.VerifyCredentials()
buffer = api.GetSearch( term='tusk',per_page=100, lang='pl', show_user='true', query_users=False)
for status in buffer:
    record['status'],record['id'],record['timestamp'] = status.GetText(),status.GetId(), status.GetCreatedAtInSeconds()
    print record
    a = hashes.models.Tweets(tweet_timestamp=record['timestamp'],tweet_id=record['id'],content=record['status'],positiveness='0.5')
    if hashes.models.Tweets.objects.filter(tweet_id=record['id']).count() == 0:
        print "Insert"
