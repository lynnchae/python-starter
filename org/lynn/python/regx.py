# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

import re

# r'' 不需要转义
regex = r'^(\d{3})-(\d{3,5})'
m = re.match(regex, '123-542')
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 未识别连续的空格
print('a b  c'.split(' '))

print(re.split(r'\s+', 'a b   c'))

regexCompiled = re.compile(r'^(\d{3})-(\d{3,5})')
print(regexCompiled.match('232-4232'))


