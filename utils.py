#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yushuibo
@licence: Copyright (c) 2017-2027, Node Supply China Manager Corporation Limited.
@contact: hengchen2005@gmail.com
@sftware: PyCharm
@site    : 
@file    : utils.py
@time: 2018/3/20 上午 11:30
@desc: --
"""

import sys
import time
import urllib.request
import urllib.parse


def get_terminal_size():
    """Get (width, height) of the current terminal."""
    try:
        import fcntl, termios, struct # fcntl module only available on Unix
        return struct.unpack('hh', fcntl.ioctl(1, termios.TIOCGWINSZ, '1234'))
    except:
        return (40, 80)

def new_tmp_file(path, size):
    with open(path, 'wb') as f:
        f.seek(size - 1)
        f.write(b'\x00')

def get_opener(https=True, proxy=False):
    if https:
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
    if proxy:
        proxy = urllib.request.ProxyHandler({'https': '127.0.0.1:8087'})
        opener = urllib.request.build_opener(proxy)
    else:
        opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    return opener

def convert_url(url):
    protocol = urllib.parse.urlsplit(url)[0]
    print('protocol is {}'.format(protocol))
    if 'http' == protocol:
        pass
    elif 'https' == protocol:
        pass
    elif 'thunder' == protocol:
        pass
    else:
        pass
