# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

import requests

r = requests.get('http://m.yinghuafenqi.com/openapi/system/getActive', headers={'userid': '1'}, timeout=2.5)
# r = requests.post('http://m.yinghuafenqi.com/openapi/system/getActive', data={'userid': '1'}, timeout=2.5)
# r = requests.post('http://m.yinghuafenqi.com/openapi/system/getActive', json={'userid': '1'}, timeout=2.5)
print(r.url)
print(r.status_code)
print(r.headers['Content-Type'])
print(r.json())

r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
