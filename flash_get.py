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


from urllib import request
from urllib import parse

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

    def pase_url(self, real_url):
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        proxy_opener = request.ProxyHandler({'https': '127.0.0.1:8087'})
        opener = request.build_opener(proxy_opener)
        request.install_opener(opener)
        headers = opener.open(real_url).headers
        print(headers)
        name = parse.unquote(real_url, encoding='utf-8').split('/')[-1]
        path = parse.urlsplit(real_url)[2]
        host = parse.urlsplit(real_url)

        print(name)
        print(path)
        print(host)


if __name__ == '__main__':
    url = 'http://issuecdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_6.0.2.exe'
    # url = 'https://dldir1.qq.com/qqfile/qq/QQ9.0.1/23161/QQ9.0.1.exe'
    # url = 'https://www.google.com/chrome/browser/thankyou.html?standalone=1&platform=win&installdataindex=defaultbrowser'
    # url='https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BA11612D1-4FA0-F3F8-B6FB-30F3918552C5%7D%26lang%3Dzh-CN%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dstable-arch_x86-statsdef_1%26installdataindex%3Ddefaultbrowser/chrome/install/ChromeStandaloneSetup.exe'
    fg = FlashGet(url)

    fg.pase_url(url)