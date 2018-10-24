from functools import reduce

# map 函数
print(list(map(str, [1, 2, 3])))


# reduce 函数

def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 4, 5]))


def normalize(x):
    x = x[:1].upper() + x[1:].lower()
    return x


print(list(map(normalize, ["tom", "arroN", "caTTER"])))
