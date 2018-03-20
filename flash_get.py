#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yushuibo
@licence: Copyright (c) 2017-2027, Node Supply China Manager Corporation Limited.
@contact: hengchen2005@gmail.com
@sftware: PyCharm
@site    : 
@file    : flash_get.py
@time: 2018/3/19 上午 11:13
@desc: --
"""


import urllib.parse

import utils
import task
import task_monitor

class FlashGet(object):

    def __init__(self, url):
        self.url = url

    def pase(self, real_url):
        scheme, netloc, path, query, fragment = urllib.parse.urlsplit(real_url)
        name = urllib.parse.unquote(path).split('/')[-1]
        length = utils.get_opener().open(real_url).headers['Content-Length']
        return name, int(length)


if __name__ == '__main__':
    # url = 'http://issuecdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_6.0.2.exe'
    url = 'https://dldir1.qq.com/qqfile/qq/QQ9.0.1/23161/QQ9.0.1.exe'
    # url = 'https://www.google.com/chrome/browser/thankyou.html?standalone=1&platform=win&installdataindex=defaultbrowser'
    # url='https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BA11612D1-4FA0-F3F8-B6FB-30F3918552C5%7D%26lang%3Dzh-CN%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dstable-arch_x86-statsdef_1%26installdataindex%3Ddefaultbrowser/chrome/install/ChromeStandaloneSetup.exe'
    fg = FlashGet(url)
    name, length = fg.pase(url)
    task = task.Task(1, url, r'{}'.format(name), length, 1)
    monitor = task_monitor.TaskMonitor()
    monitor.tasks.append(task)
    monitor.start()
    task.start()



