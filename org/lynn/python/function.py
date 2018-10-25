#!/usr/bin/env python3
nums = [1, 2, 3]
print(max(nums))

print(bool(''))
print(bool(1))


def test(x):
    if not isinstance(x, (int, float)):
        raise TypeError('not a number')
    if x % 2 == 0:
        print('偶数')
    else:
        print('奇数')


def nop():
    pass


test(12)

nop()


# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是设置默认参数,把变化大的参数放前面，变化小的参数放后面
# 默认参数必须指向不变对象！


def power(x, n=2):
    p = 1
    while n > 0:
        n = n - 1
        p = p * x
    return p


print(power(2))


# 可变参数
def clac(*numbers):
    s = 0
    for number in numbers:
        s = s + number * number
    print('平方和为：' + str(s))


nms = [1, 2, 3]
clac(nms[0], nums[1], nums[2])
clac(*nms)


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'beijing', 'job': 'sweeper'}

person('Jack', 19, city='beijing', job='sweeper')
person('Jack', 19, **extra)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1())

# 匿名函数
print(list(map(lambda x: x * x, [1, 2, 3, 4])))
