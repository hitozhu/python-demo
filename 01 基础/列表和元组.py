#! /usr/bin/python
# -*- coding: utf8 -*-

# 列表
fruits = ['banana', 'apple', 'pineapple', 'peach']
print(fruits)
print(len(fruits))
print(fruits[1])

# index  -1 代表去最后一个
print(fruits[-1])

# append and insert
fruits.append('watermelon')
print(fruits)

fruits.insert(1, 'strawberry')
print(fruits)

# pop 删除
# last one
fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

# 元素替换
fruits[2] = 'strawberry'
print(fruits)


print('''
------------元组------------
''')
# 元组 tuple， 元组一旦初始化元素不可变，不可变指指向的地址不变
t = ('1', 2, '3')
print(t)

t2 = ('aa', [111, 222], 'cc')
print(t2)
t2[1][0] = 333
t2[1][1] = 444
print(t2)