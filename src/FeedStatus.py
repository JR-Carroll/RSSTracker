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
        for feed in range(0, len(bulk_feeds), 1):
            value = bulk_feeds[feed]
            for i in all_feeds:
                if i['id'] == int(value):
                    url = i['URL']
                    try:
                        self.connectDB.check_feed(id=value)
                        
                    except:
                        raise
                else:
                    pass
            
    def activate(self, bulk_feeds):
        for i in bulk_feeds:
            self.connectDB.activate_feed(i)
            
    def deactivate(self, bulk_feeds):
        for i in bulk_feeds:
            self.connectDB.deactivate_feed(i)
                   

class FeedInformation():
    def __init__(self, feedURL):
        self.name = feedURL
        self.url = feedURL
        self.titles = []
        self.contents = []
        self.authors = []
        
        setattr(self, "__name__", "My object")
        print dir(feedparser)
        self.feed_info = feedparser.parse(self.url)
    
    def feed_split(self):
        
        for i in self.feed_info(): 
            self.titles.append(self.feed_info['title'])
            self.contents.append(self.feed_info['content'])
            self.authors.append(self.feed_info['author'])
