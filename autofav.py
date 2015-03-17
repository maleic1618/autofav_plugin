#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os
sys.path.append(os.pardir)

from plugin import *

class auto_favorite(Plugin):
    def __init__(self,mainwindow):
        super(auto_favorite,self).__init__(mainwindow)
        self.screen_name=u'tara_nai'

    def on_status(self, status):
        if status.has_key('event') == False:
            if status.has_key('text') == True:
                if status['user']['screen_name'] == self.screen_name:
                    self.create_favorite(status['id'])
