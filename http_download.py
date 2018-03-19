#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yushuibo
@licence: Copyright (c) 2017-2027, Node Supply China Manager Corporation Limited.
@contact: hengchen2005@gmail.com
@sftware: PyCharm
@site    : 
@file    : http_download.py
@time: 2018/3/19 上午 10:28
@desc: --
"""

import threading


class HttpDownLoader(threading.Thread):

    def __init__(self, opener, start_pos, end_pos):
        threading.Thread.__init__(self)
        self.opener = opener
        self.start_pos = start_pos
        self.end_pos = end_pos

    def download(self):
        pass

    def run(self):
        self.download()