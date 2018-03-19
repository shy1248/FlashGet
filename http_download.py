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


import os
import threading


class HttpDownLoader(threading.Thread):

    def __init__(self, opener, url, start_pos, end_pos, dest_file):
        threading.Thread.__init__(self)
        self.opener = opener
        self.url = url
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.dest_file = dest_file

    def download(self):
        self.opener.addheaders = [('Range', 'bytes={}-{}'.format(self.start_pos, self.end_pos))]
        url_handler = self.opener.open(self.url)
        buffer_size = 1024
        offset = self.start_pos
        buffer = url_handler.read(buffer_size)
        while buffer:
            with open(self.dest_file, 'wb') as fh:
                fh.seek(offset, os.SEEK_SET)
                fh.write(buffer)
                offset += len(buffer)
                buffer = url_handler.read(buffer_size)

    def run(self):
        self.download()