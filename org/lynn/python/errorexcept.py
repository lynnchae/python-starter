# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

def test_error(x):
    result = 0
    try:
        result = 10 / x
    except ZeroDivisionError as e:
        print('ZeroDivisionError:',e)
    finally:
        print('finally end')
    return result

print(test_error(0))
