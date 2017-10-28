#save this file as 'tweet.py'


import tweepy

from keys import *

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey,asecret)

api = tweepy.API(auth)

api.update_status('  //Your message goes here..//  ')
