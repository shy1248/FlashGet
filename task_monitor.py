#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yushuibo
@licence: Copyright (c) 2017-2027, Node Supply China Manager Corporation Limited.
@contact: hengchen2005@gmail.com
@sftware: PyCharm
@site    : 
@file    : task_monitor.py
@time: 2018/3/20 下午 04:49
@desc: --
"""


import threading
import time

class TaskMonitor(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.tasks = []

    def run(self):
        for task in self.tasks:
            task.update_msg()
