# !/usr/bin/env python
# -*- coding:utf-8 -*-
# 小红书微信小程序 X-Sign

import hashlib


def get_sign(url):
    add_salt = url.split("www.xiaohongshu.com")[1] + "WSUDD"
    Sign = "X" + hashlib.md5(add_salt.encode("utf-8")).hexdigest()
    return Sign
