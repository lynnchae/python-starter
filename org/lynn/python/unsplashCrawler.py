# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

from contextlib import closing
import requests

req = requests.get('https://unsplash.com/napi/photos?page=1&per_page=12&order_by=latest')
for x in req.json():
    url = 'https://unsplash.com/photos/xxx/download?force=true'.replace('xxx', x['id'])
    with closing(requests.get(url=url, stream=True, verify=False)) as r:
        with open('%s.jpg' % x['id'], 'ab+') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
