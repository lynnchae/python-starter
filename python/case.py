#!/usr/bin/env python3
# -*- coding:utf-8 -*-
age = int(input('please input your age!'))
if age >= 18:
    print("you are a adult , {0} ".format(age))
elif age > 6:
    print('teenager')
else:
    print('kid')

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
height = float(input('enter you height(m) : '))
weight = float(input('enter you weight(kg): '))
bmi = weight / (height * height)
print('your bmi is :', bmi)
if bmi > 32:
    print("严重肥胖")
elif bmi >= 28:
    print("肥胖")
elif bmi >= 25:
    print("过重")
elif bmi >= 18.5:
    print("正常")
else:
    print("过轻")
