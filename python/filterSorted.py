def is_odd(x):
    return x % 2 == 0


numbers = list(range(15))

print(list(filter(is_odd, numbers)))

aStr = ' test '
print('-' + aStr.strip() + '-')

print(sorted([1, 5, 12, -12, -3, 56], key=abs))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(t):
    return t[1]


def by_name(t):
    return t[0]


print(sorted(L, key=by_score, reverse=False))
print(sorted(L, key=by_name))
