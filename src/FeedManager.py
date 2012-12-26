#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Dec 25, 2012

@author: J Carroll
@emaill: jrcarroll@jrcresearch.net
'''

import wx

class FeedWindow(wx.App):
    def OnInit(self):
        wx.MessageBox("This program is designed to capture syndication feeds " \
        "ONLY. This application will not allow you reply to new posts, but " \
        "you can use it to track what's been read and what has not been read. " \
        "If you have any questions or comments (especially bugs) please report " \
        "them to jrcarroll@jrcresearch.net", 
        'wxApp')
        return True


if __name__ == '__main__':
    app = FeedWindow(False)
    app.MainLoop()
