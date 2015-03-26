#!/usr/bin/env python

__author__ = 'Kryptic Mind'

import daemon

class TwitterBot():

    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path = '/var/run/twitter_bot.pid'
        self.pidfile_timeout = 5

    def run(self):
        pass

app = TwitterBot()
daemon_runner = daemon.runner.DaemonRunner(app)
daemon_runner.do_action()