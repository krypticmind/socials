#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'Kryptic Mind'

import json

from tweepy import OAuthHandler, API, Stream
from tweepy.streaming import StreamListener

TWEETS_IN_BATCH = 10

class TwitterBot():

    def __init__(self, consumer_key=None, consumer_secret=None, access_token=None, access_token_secret=None):
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = API(auth_handler=self.auth)

    def stream(self, stream_log):
        with open(stream_log, "w") as stream_file:
            twitterStream = Stream(self.auth, Listener(stream_file))
            twitterStream.filter(track=[u"music", u"музыка"])

    def post(self, text):
        self.api.update_status(status=text)


class Listener(StreamListener):

    def __init__(self, stream_file):
        self.stream_file = stream_file
        self.tweets_batch = []

    def on_data(self, data):
        self.stream_file.write(data)
        self.tweets_batch.append(data)
        if len(self.tweets_batch) >= TWEETS_IN_BATCH:
            self.process_batch(self.tweets_batch)
            del self.tweets_batch[:]
        return True

    def process_batch(self, batch):
        print "Process batch, {0} item(s)".format(len(batch))
        for tweet_json in batch:
            tweet = json.loads(tweet_json)
            print tweet["text"]

    def on_error(self, status_code):
        print status_code
