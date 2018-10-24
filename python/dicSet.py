#!/usr/bin/env python3
dicts = {'Michael': 19, 'Lynn': 29,'SB':10}
print(dicts['Michael'])
dicts.pop('SB')
print(dicts)
dicts.setdefault('Jabz',19)
dicts['IceIceIce'] = 25
print(dicts)

# 判断key是否存在dict中
if 'M' in dicts:
    print("exists")
else:
    print('not exists')

ele = dicts.get('M')
print(ele)

## set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
## 要创建一个set，需要提供一个list作为输入集合
sets = set([1, 2, 3])

sets.add(4)
print(sets)