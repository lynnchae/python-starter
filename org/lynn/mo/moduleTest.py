#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'module test'

__author__ = 'Cailinfeng'

import sys


def test():
    args = sys.argv
    print('method call args : ', args)
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# 私有变量或者方法
_local_variable = 'private'

_local_variable_v2 = 'private2'


def _private_method(x):
    print(x)


if __name__ == '__main__':
    test()
