#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Kryptic Mind'

import core

from ConfigParser import ConfigParser
# from daemon import DaemonContext

config = ConfigParser()
config.read('config.ini')

CONSUMER_KEY = config.get("ConsumerTokens", "CONSUMER_KEY")
CONSUMER_SECRET = config.get("ConsumerTokens", "CONSUMER_SECRET")
ACCESS_TOKEN = config.get("AccessTokens", "ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = config.get("AccessTokens", "ACCESS_TOKEN_SECRET")

if __name__ == '__main__':
    bot = core.TwitterBot(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    bot.stream()
