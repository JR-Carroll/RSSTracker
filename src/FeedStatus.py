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
        self.URLposition = {}
        
    def del_feeds(self, bulk_feeds):
        for i in bulk_feeds:
            print "this printed -->", i
            self.connectDB.del_feedBY('id', i)
    
    def check_feeds(self, all_feeds, bulk_feeds):
        for feed in range(0, len(bulk_feeds), 1):
            print feed
            self.URLposition[feed] = all_feeds['id']['URL']
            print "this is it!!!!!!!!!!!!!!!!!!!!!!!!!", self.URLposition
#            self.URL = i
#            self.feed = feedparser.parse(eval(self.URL))
#            
#            self.title = feed['feed']['title']
#            self.link = feed['feed']['link']
#            self.status = feed['status']
#            self.encoding = feed['encoding']
#            
#            for i in self.feed['entries']:
#                print i.keys()
#                break
#            print self.feed['entries'][3]['content']
#            print self.title
#            print self.link