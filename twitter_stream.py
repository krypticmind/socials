#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Kryptic Mind'

from ConfigParser import ConfigParser
from tweepy.streaming import StreamListener
import daemon

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
    bot = daemon.TwitterBot(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    bot.stream()
