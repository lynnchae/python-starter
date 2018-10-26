# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

from datetime import datetime, timedelta

nowtime = datetime.now()
print(nowtime)
print(nowtime.timestamp())

dt = datetime(2018, 12, 25, 19, 17, 22)
print(dt)

# 字符串转时间
stime = datetime.strptime('2018-09-10 12:19:01', '%Y-%m-%d %H:%M:%S')
print(stime)

# 日期转字符串
print(nowtime.strftime('%a, %b %d %H:%M'))

# 日期加减
print(nowtime + timedelta(hours=5))
print(nowtime + timedelta(days=5))
print(nowtime + timedelta(seconds=5))
print(nowtime + timedelta(minutes=5))
