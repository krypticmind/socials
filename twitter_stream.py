#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Kryptic Mind'

from ConfigParser import ConfigParser
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


config = ConfigParser()
config.read('config.ini')

CONSUMER_KEY = config.get("ConsumerTokens", "CONSUMER_KEY")
CONSUMER_SECRET = config.get("ConsumerTokens", "CONSUMER_SECRET")
ACCESS_TOKEN = config.get("AccessTokens", "ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = config.get("AccessTokens", "ACCESS_TOKEN_SECRET")

class Listener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self, status_code):
        print status_code

if __name__ == '__main__':
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    twitterStream = Stream(auth, Listener())
    twitterStream.filter(track=[u"music", u"музыка"])