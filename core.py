#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yushuibo
@licence: Copyright (c) 2017-2027, Node Supply China Manager Corporation Limited.
@contact: hengchen2005@gmail.com
@sftware: PyCharm
@site    : 
@file    : core.py
@time: 2018/3/19 上午 10:28
@desc: --
"""

import os
import threading

import utils


class HttpDownLoader(threading.Thread):

    def __init__(self, task, url, start_pos, end_pos, dest_file):
        threading.Thread.__init__(self)
        self.task = task
        self.url = url
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.dest_file = dest_file
        self._lock = threading.Lock()
        self.__flag = threading.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()

    def download(self):
        # print('Thread-{}@Task-{}: downloading with start position is {} and end postion is {}.'.format(self.start_pos,
        #                                                                                                self.task.id,
        #                                                                                                self.start_pos,
        #                                                                                                self.end_pos))
        opener = utils.get_opener()
        if self.task.threads_num > 1:
            opener.addheaders = [('Range', 'bytes={}-{}'.format(self.start_pos, self.end_pos))]
        url_handler = opener.open(self.url)
        buffer_size = 1024
        offset = self.start_pos
        buffer = url_handler.read(buffer_size)
        f = open(self.dest_file, 'rb+')
        while buffer:
            with self._lock:
                self.task.downloaded += len(buffer)
            f.seek(offset, os.SEEK_SET)
            f.write(buffer)
            f.flush()
            offset += len(buffer)
            buffer = url_handler.read(buffer_size)
        f.close()

    def run(self):
        self.download()

    def pause(self):
        self.__flag.clear()

    def resum(self):
        self.__flag.set()

    def stop(self):
        self.__flag.set()
        self.__running.clear()
