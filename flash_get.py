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


import os
import random
from urllib import request
from urllib import parse

from http_download import HttpDownLoader

class FlashGet(object):

    def __init__(self, url):
        self.url = url

    def convert_url(self):
        protecol = self.url.split('://')[0]
        print(protecol)
        if 'http' in protecol:
            pass
        elif 'thunder' in protecol:
            pass
        else:
            pass

    def get_opener(self):
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        proxy_opener = request.ProxyHandler({'https': '127.0.0.1:8087'})
        opener = request.build_opener(proxy_opener)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        request.install_opener(opener)
        return opener

    def pase_url(self, real_url):
        path = parse.urlsplit(real_url)[2]
        name = path.split('/')[-1]
        headers = self.get_opener().open(real_url).headers
        length = headers['Content-Length']
        return name, path, length


    def create_tmp_file(self, path, size):
        with open(path, 'wb') as f:
            f.seek(size - 1)
            f.write(b'\x00')


if __name__ == '__main__':
    url = 'http://issuecdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_6.0.2.exe'
    # url = 'https://dldir1.qq.com/qqfile/qq/QQ9.0.1/23161/QQ9.0.1.exe'
    # url = 'https://www.google.com/chrome/browser/thankyou.html?standalone=1&platform=win&installdataindex=defaultbrowser'
    # url='https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BA11612D1-4FA0-F3F8-B6FB-30F3918552C5%7D%26lang%3Dzh-CN%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dstable-arch_x86-statsdef_1%26installdataindex%3Ddefaultbrowser/chrome/install/ChromeStandaloneSetup.exe'
    fg = FlashGet(url)
    name, path, length = fg.pase_url(url)
    length = int(length)
    # fg.create_tmp_file(name, length)
    print('length={}'.format(length))
    max_thread = 10
    cal = divmod(length, max_thread)
    if cal[1] == 0:
        block_size = cal[0]
        for i in range(0, max_thread):
            downloader = HttpDownLoader(fg.get_opener(), url, i*block_size, (i+1)*block_size, name)
            downloader.start()
    else:
        block_size = divmod(length, max_thread+1)[0]
        print('block_size={}'.format(block_size))
        for i in range(0, max_thread):
            if i < max_thread - 1:
                print('i={}, start={}, end={}'.format(i, i*block_size, (i+1)*block_size))
                downloader = HttpDownLoader(fg.get_opener(), url, i*block_size, (i+1)*block_size, name)
                downloader.start()
            else:
                print('i={}, start={}, end={}'.format(i, i * block_size, length))
                downloader = HttpDownLoader(fg.get_opener(), url, i*block_size, length, name)
                downloader.start()



