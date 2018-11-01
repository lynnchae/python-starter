#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
a = '123'
print(a)

A = 'COW BOY'
B = A
A = 'CRAZY BOY'
print(B)

print(10 / 3)
# 地板除
print(10 // 3)

print('中文')

# 如果不知道类型，可以永远使用%s做格式化占位符
# name = input()
# print("hello, %s!" % name)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# List 有序集合
classmates = ['Tom', 'Jack', 'Jason']
print(classmates[0])
print(classmates[1])
# 倒数第一个
print(classmates[-1])
# 追加
classmates.append('Sara')
print(classmates)

# 在索引位置插入
classmates.insert(1, 'Bob')
print(classmates)
# 获取并删除最后一个
classmates.pop()
print(classmates)

# 获取并删除索引位元素
classmates.pop(1)
print(classmates)

# list长度
print(len(classmates))

differentEleList = ['String', 120, True]
print(differentEleList)

# Tuple 类似list，但不可变
aTuple = ('Job', 'Age', 'Height')
# 只有1个元素的tuple定义时必须加一个逗号,
bTuple = (1,)

for i in range(10):
    for j in range(1, i + 1):
        print('%s * %s = %s ' % (j, i, j * i), end=" ")
    print()
