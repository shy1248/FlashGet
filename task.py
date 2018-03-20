#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yushuibo
@licence: Copyright (c) 2017-2027, Node Supply China Manager Corporation Limited.
@contact: hengchen2005@gmail.com
@sftware: PyCharm
@site    : 
@file    : task.py
@time: 2018/3/20 上午 10:35
@desc: --
"""


import time
import sys

import utils
from core import HttpDownLoader


class Task(object):

    def __init__(self, id, url, file, length, threads_num):
        self.id = id
        self.url = url
        self.file = file
        self.length = length
        self.threads_num = threads_num if threads_num else 10
        self.threads = []
        self.downloaded = 0
        self.is_alive = False
        self._bar = self.SimpleProgressBar(self.length)
        self.init()

    def init(self):
        self.out_summary()
        utils.new_tmp_file(self.file, self.length)
        t = divmod(self.length, self.threads_num)
        block_size = t[0]
        for i in range(self.threads_num):
            downloader = HttpDownLoader(self, self.url, i * block_size, (i + 1) * block_size, self.file)
            self.threads.append(downloader)
        if t[1] != 0:
            downloader = HttpDownLoader(self, self.url, self.threads_num * block_size, self.length, self.file)
            self.threads.append(downloader)

    def delete(self):
        pass

    def is_done(self):
        return True if self.downloaded >= self.length else False

    def start(self):
        for t in self.threads:
            t.start()
        self.is_alive = True

    def pause(self):
        for t in self.threads:
            t.pause()
        self._is_alive = False

    def resum(self):
        for t in self.threads:
            t.resum()

    def out_summary(self):
        print('Start new download task:')
        # print('Source URL:\n{}'.format(self.url))
        print('URL:\t{}'.format(self.url))
        print('File Name:\t{}'.format(self.file))
        print('File Length:\t{}'.format(self.length))
        print('Procgress:')



    def update_msg(self):
        last_downloaded = 0
        while True:
            self._bar.update_received(self.downloaded - last_downloaded)
            last_downloaded = self.downloaded
            time.sleep(1)
            if last_downloaded >= self.length:
                self._bar.done()
                print('Task is done!')
                break


    class SimpleProgressBar:
        term_size = utils.get_terminal_size()[1]

        def __init__(self, total_size):
            self.displayed = False
            self.total_size = total_size
            self.received = 0
            self.speed = ''
            self.last_updated = time.time()

            # 38 is the size of all statically known size in self.bar
            total_str = '%5s' % round(self.total_size / 1048576, 1)
            total_str_width = max(len(total_str), 5)
            self.bar_size = self.term_size - 28 - 2 * total_str_width
            self.bar = '{:>4}%% ({:>%s}/%sMB) ├{:─<%s}┤ {}' % (
                total_str_width, total_str, self.bar_size
            )

        def update(self):
            self.displayed = True
            bar_size = self.bar_size
            percent = round(self.received * 100 / self.total_size, 1)
            if percent >= 100:
                percent = 100
            dots = bar_size * int(percent) // 100
            plus = int(percent) - dots // bar_size * 100
            if plus > 0.8:
                plus = '█'
            elif plus > 0.4:
                plus = '>'
            else:
                plus = ''
            bar = '█' * dots + plus
            bar = self.bar.format(
                percent, round(self.received / 1048576, 1), bar, self.speed
            )
            sys.stdout.write('\r' + bar)
            sys.stdout.flush()

        def update_received(self, n):
            self.received += n
            time_diff = time.time() - self.last_updated
            bytes_ps = n / time_diff if time_diff else 0
            if bytes_ps >= 1024 ** 3:
                self.speed = '{:4.0f} GB/s'.format(bytes_ps / 1024 ** 3)
            elif bytes_ps >= 1024 ** 2:
                self.speed = '{:4.0f} MB/s'.format(bytes_ps / 1024 ** 2)
            elif bytes_ps >= 1024:
                self.speed = '{:4.0f} kB/s'.format(bytes_ps / 1024)
            else:
                self.speed = '{:4.0f}  B/s'.format(bytes_ps)
            self.last_updated = time.time()
            self.update()

        def done(self):
            if self.displayed:
                print()
                self.displayed = False
