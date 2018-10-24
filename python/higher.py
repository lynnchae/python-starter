#!/usr/bin/env python3
names = ['Michael', 'Lily', 'Tom', 'Jack', 'Mingming']
print(names[0:3])
print(names[:3])

numbers = list(range(101))
# 取前面10个数，每两个取一个
print(numbers[:10:2])


# tuple str都可以使用此操作

def trim(s):
    if not len(s):
        raise ValueError('empty str')
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return '<' + s + '>'


print(trim(' hello world!    '))

dicts = {'Gaby': 10, 'Lily': 12, 'Jason': 11}
for k in dicts:
    print(k)

for v in dicts.values():
    print(v)

for k, v in dicts.items():
    print(k, ':', v)

for s in 'ABCD':
    print(s)

print([x * x for x in list(range(1, 11))])

lists = ["Hello", "Python", 19]

print([x.lower() for x in lists if isinstance(x, str)])

'''a, b = b, a + b 先计算右边运算，然后再赋值
   a = b , b = a + b 输出结果就不同了
'''


def fib(val):
    n, a, b = 0, 0, 1
    while n < val:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print([x for x in fib(3)])
