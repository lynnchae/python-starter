# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

f = open('../../../venv/pip-selfcheck.json', 'r')

try:
    f = open('../../../venv/pip-selfcheck.json', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 等效上面代码 如果读取二进制文件  参数 r -> rb
with open('../../../venv/pip-selfcheck.json', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line)

with open('t.txt', 'w') as f:
    f.write('hello python')
