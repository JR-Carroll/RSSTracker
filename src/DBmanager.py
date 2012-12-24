#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Dec 23, 2012

@author: J Carroll
@emaill: jrcarroll@jrcresearch.net
'''

import sqlite3 as sq
from datetime import datetime

__DB_NAME__ = 'FeedDB.db'
__DB_TABLE__ = 'feeds'


class FeedDatabase():
    def __init__(self):
        """
        Connects to the database and adds a table as necessary
        """
        
        global __DB_NAME__
        global __DB_TABLE__
        
        self.__db__ = __DB_NAME__
        self.db = sq.connect(self.__db__)
        self.table = __DB_TABLE__
        self.cursor = self.db.cursor()
        self.create_table(self.table)
        
    def create_table(self, table):
        """
        Attempts to create the main feeds table - if it does not exists, it will
        make it
        """

        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS " + 
                           __DB_TABLE__ + 
                           "(id INTEGER PRIMARY KEY, URL TEXT, Active INTEGER DEFAULT 0, Added TEXT, Last_Checked TEXT DEFAULT 'Never Checked')")
        except:
            raise
    
    def add_feed(self, URL):
        """Add a feed"""
        
        self.__sql_add__ = "INSERT INTO feeds (URL, Active, Added) VALUES (\"{0}\", {1}, \"{2}\")".format(URL, 
                                                                                                          1, 
                                                                                                          datetime.ctime(datetime.now()))
        self.cursor.execute(self.__sql_add__)
        self.db.commit()
        
    def activate_feed(self, URL):
        """Activate feeds"""
        self.__sql_update__ = "UPDATE feeds SET Active = 1 WHERE URL = \"{0}\" AND Active = 0".format(URL)
        self.cursor.execute(self.__sql_update__)
        self.db.commit()
            
    def deactivate_feed(self, URL):
        """Deactivate an active feed"""
        self.__sql_update__ = "UPDATE feeds SET Active = 0 WHERE URL = \"{0}\" AND Active = 1".format(URL)
        self.cursor.execute(self.__sql_update__)
        self.db.commit()
    
    def all_feeds(self):
        """Return a generator object that contains all the feed detail"""
        all_feeds = self.cursor.execute("SELECT * from feeds")
        return all_feeds

    def del_feedBY(self, column, value):
        sql_del = "DELETE FROM {0} WHERE {1} = {2}".format(self.table, column, value)
        self.cursor.execute(sql_del)
        self.db.commit()

if __name__ == '__main__':
    v = FeedDatabase()
    v.add_feed("http://hhateyou.com")
#    v.add_feed("http://jrcresearch.net")
#    v.add_feed("bob.net")
#    
#    feeds = ["just.com", "katy.com", "eric.com", "jan.com"]
    
#    for url in feeds:
#        v.add_feed(url)
        
    for i in v.all_feeds():
        print i
    
    v.del_feedBY(id, "28")
    