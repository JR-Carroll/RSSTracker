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

URL = ConnectFeedDB()
URL = URL.select_feed('id', '1')[0][2]

feed = feedparser.parse(eval(URL))

title = feed['feed']['title']
link = feed['feed']['link']
status = feed['status']
encoding = feed['encoding']
for i in feed['entries']:
    print i.keys()
    break
print feed['entries'][3]['content']
print title
print link

#for i in feed['entries']:
#    print i
#    break
#
#print len(feed.entries[0].enclosures)
#print feed['entries'][0].keys()
#
#print feed['entries'][0]['summary']







