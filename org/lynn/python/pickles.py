# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

import pickle
import json

# 二进制序列化
d = dict(name='bob', age=12)
dpickle = pickle.dumps(d)
print(pickle.loads(dpickle))
# f = open('dump.txt', 'wb')
# pickle.dumps(d,f)
# f.close()

djson = json.dumps(d)
print(json.loads(djson))

