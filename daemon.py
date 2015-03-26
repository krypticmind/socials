#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'Kryptic Mind'

from tweepy import OAuthHandler, API, Stream
from tweepy.streaming import StreamListener


class TwitterBot():
    def __init__(self, consumer_key=None, consumer_secret=None, access_token=None, access_token_secret=None):
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = API(auth_handler=self.auth)

    def stream(self):
        twitterStream = Stream(self.auth, Listener())
        twitterStream.filter(track=[u"music", u"музыка"])

    def post(self, text):
        self.api.update_status(status=text)


class Listener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self, status_code):
        print status_code
