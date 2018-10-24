#!/usr/bin/env python3
from collections import Iterable
names = ['Micheal', 'Tom', 'Json']
for name in names:
    print(name)

# range(5) 生成0~4整数序列
# for 循环
numbers = list(range(5))
sum = 0
for number in numbers:
    if number % 2 == 0:
        continue
    sum = sum + number
print(sum)

# while 循环
sum = 0
n = 0
while n < 10:
    if n == 5:
        break
    sum = sum + n
    n = n + 1
print(sum)

print(isinstance(names,Iterable))