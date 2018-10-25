#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import functools

# 将1001按二进制转换为10进制数
print(int('1001', base=2))


def int2(x):
    return int(x, base=2)


print(int2('1001010101'))

# 偏函数，将某些参数固定，简化方法
int2V = functools.partial(int, base=2)

print(int2V('10101101'))
