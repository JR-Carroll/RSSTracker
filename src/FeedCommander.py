#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Dec 28, 2012

@author: J Carroll
@emaill: jrcarroll@jrcresearch.net
'''

import cgi 
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

from DBmanager import ConnectFeedDB

feeds = ConnectFeedDB()

class Feeds(Resource):
    def __init__(self):
        Resource.__init__(self)
        self.value = "test"
        self.html = self.create_html()
        self.feed_gen = [x for x in feeds.all_feeds()]
        self.feeds = ""
        self.all_feeds()
        
    def create_html(self):    
        self.html = """
        <html>
        <body bgcolor="black" text="white">
        <form name="feeds" method=POST> 
        <table border=2 cellpadding=5>
            <tr>
                <td>Select</td>
                <td>Feed ID</td>
                <td>Feed Type</td>
                <td>URL</td>
                <td>Active?</td>
                <td>Date Added</td>
                <td>Date Last Checked</td>
            </tr>
            {0} 
        </table>
        
        Bulk Action: <select name="BulkAction">
        <option value="delete_feeds">Delete Feed(s)</option>
        <option value="check_now">Check Now</option>
        <option value="activate">Activate</option>
        <option value="deactivate">Deactivate</option>
        </select>
        </form>
        </body>
        </html>"""
        
        return self.html
    
    def all_feeds(self):
        print self.feed_gen
        for i in self.feed_gen:
            self.feeds += "<tr>\n\t<td><input type=\"checkbox\" name=\"index_{0}\" value=\"selected_feed\"/>".format(i[0])
            
            for element in i:
                self.feeds += "<td>" + str(element) + "</td>"
            
            self.feeds += "</tr>"
            
    def inject_feeds(self):
        self.html = self.html.format(self.feeds)
        return self.html
    
    def render_GET(self, request):
        return self.inject_feeds()
    
    def render_POST(self, request):
        return cgi.escape(request.args['the-field'][0])
            
class ServeFeeds(Resource):
    def getChild(self, name, request):
        return Feeds()

v = Feeds()
v.all_feeds()

root = ServeFeeds()
factory = Site(root)
reactor.listenTCP(8777, factory)
reactor.run()
