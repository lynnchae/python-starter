# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# 它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 12)
print(p.x)
print(p.y)

q = deque([1, 2, 3])
q.append(4)
q.appendleft(0)
print(q)

dd = defaultdict(lambda: 'not exists')
dd['key1'] = 'value1'
print(dd['key1'])
print(dd['key2'])

od = OrderedDict([('z', 1), ('y', 2), ('x', 3)])
dic = dict([('z', 1), ('y', 2), ('x', 3)])
print(od)
print(dic)

c = Counter()
for i in 'zxcfdfdcxd':
    c[i] += 1
print(c)
