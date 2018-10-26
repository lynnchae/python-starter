# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

import hashlib, hmac

md5 = hashlib.md5()
md5.update('hello world!'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('hello world!'.encode('utf-8'))
print(sha1.hexdigest())

string = b'hello moto'
key = b'910111'
h = hmac.new(key, string, digestmod='MD5')
print(h.hexdigest())
