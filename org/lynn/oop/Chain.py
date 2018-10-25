# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

    # 定义此函数后，实例对象可以当函数调用
    def __call__(self, *args, **kwargs):
        print('Chain is called')

print(Chain().status.user.limit.list)

c = Chain()

c()
# callable(object) 判断对象是否可被调用
print(callable(c))