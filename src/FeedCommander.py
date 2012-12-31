#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Dec 28, 2012

@author: J Carroll
@emaill: jrcarroll@jrcresearch.net
'''

#created the return value from the DB to simulate data for testing/debugging
#mockDB = [{u'Added': u'Wed Dec 26 01:09:25 2012', u'URL': u"'https://github.com/nammer?tab=activity'", u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 1}, {u'Added': u'Sat Dec 29 00:14:26 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 2}, {u'Added': u'Sat Dec 29 00:14:31 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 3}, {u'Added': u'Sat Dec 29 00:14:33 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 4}, {u'Added': u'Sat Dec 29 00:14:34 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 5}, {u'Added': u'Sat Dec 29 00:14:42 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 6}, {u'Added': u'Sat Dec 29 00:14:54 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 7}, {u'Added': u'Sat Dec 29 00:15:05 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 8}, {u'Added': u'Sat Dec 29 00:24:11 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 9}, {u'Added': u'Sat Dec 29 16:23:35 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 10}, {u'Added': u'Sat Dec 29 16:23:36 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 11}, {u'Added': u'Sat Dec 29 16:23:37 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 12}, {u'Added': u'Sat Dec 29 16:23:38 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 13}, {u'Added': u'Sat Dec 29 16:23:39 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 14}, {u'Added': u'Sat Dec 29 16:23:40 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 15}, {u'Added': u'Sat Dec 29 17:35:09 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 16}, {u'Added': u'Sat Dec 29 17:35:31 2012', u'URL': u'http://www.ccc.com', u'URIType': u'RSS', u'Last_Checked': u'Never Checked', u'Active': 1, u'id': 17}]

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
        self.feed_gen = [x for x in feeds.return_all_feeds()]
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
        for i in self.feed_gen:
            self.feeds += "<tr>\n\t<td><input type=\"checkbox\" name=\"index_{0}\" value=\"selected_feed\"/>".format(i['id'])
            v = i.keys()
            keys_ordered = ('id', 'URIType', 'URL', 'Active', 'Added', 'Last_Checked')

            for key in keys_ordered:
                self.feeds += "<td>" + str(i[key]) + "</td>"
            
            self.feeds += "</tr>"
            
    def inject_feeds(self):
        print "inject ran!"
        print self.feeds
        self.html = self.html.format(self.feeds)
        return self.html
    
    def render_GET(self, request):
        if request.path == '/feeds':
            return self.inject_feeds()
    
    def render_POST(self, request):
        return cgi.escape(request.args['the-field'][0])
            
class ServeFeeds(Resource):
    def render_GET(self, request):
        if request.path == "/feeds":
            return Feeds()
        else:
            print "and this broke but it really worked"
        
    def getChild(self, name, request):
        return Feeds()

root = Resource()
root.putChild('feeds', Feeds())
factory = Site(root)

# pylint: disable=E1101
reactor.listenTCP(8777, factory)

try:
    print "Server Running..."
    # pylint: disable=W0702
    reactor.run()
except:
    print "failed with error"
    
