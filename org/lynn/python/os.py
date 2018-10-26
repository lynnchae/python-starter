# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

import os

print(os.name)
print(os.environ.get('PATH'))

print(os.path.abspath('.'))
print(os.path.join('.', 'newDir'))
# print(os.mkdir('./testDir'))
# print(os.rmdir('./testDir'))

print(os.path.split('./os.py'))
print(os.path.splitext('./os.py'))

# 文件重命名和删除
# os.rename('','')
# os.remove('')

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([z for z in os.listdir('.') if os.path.isfile(z) and os.path.splitext(z)[1] == '.py' ])