#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Dec 23, 2012

@author: J Carroll
@emaill: jrcarroll@jrcresearch.net
'''

import feedparser

# pylint: disable=F0401
from DBmanager import ConnectFeedDB

class ModifyFeed():
    def __init__(self):
        self.connectDB = ConnectFeedDB()
        
    def mod(self, all_feeds, bulk_feeds, action):
#        print "all feeds", all_feeds
#        print "bulk feeds", bulk_feeds
#        print "action", action
        
        self.all = all_feeds
        self.bulk_feeds = bulk_feeds
        
        for feed in range(0, len(self.bulk_feeds), 1):
            value = bulk_feeds[feed]
            for i in self.all:
                if i['id'] == int(value):
                    i['URL']
                else:
                    pass
        
        if action == 'delete_feeds':
            self.del_feeds(self.bulk_feeds)
        elif action == 'check_now':
            print "check now ran"
            self.check_feeds(self.all, self.bulk_feeds)
        elif action == 'activate':
            self.activate(self.bulk_feeds)
        elif action == 'deactivate':
            self.deactivate(self.bulk_feeds)
        else:
            print action
    def del_feeds(self, bulk_feeds):
        for i in bulk_feeds:
            self.connectDB.del_feedBY('id', i)
    
    def check_feeds(self, all_feeds, bulk_feeds):
        print "check_feeds function ran"
        for feed in range(0, len(bulk_feeds), 1):
            value = bulk_feeds[feed]
            for i in all_feeds:
                if i['id'] == int(value):
                    v = i['URL']
                else:
                    pass
            return v

    def activate(self, bulk_feeds):
        for i in bulk_feeds:
            self.connectDB.activate_feed(i)
            
    def deactivate(self, bulk_feeds):
        for i in bulk_feeds:
            self.connectDB.deactivate_feed(i)
            