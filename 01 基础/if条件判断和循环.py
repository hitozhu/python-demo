#! /usr/bin/python
# -*- coding: utf8 -*-

# age = input('input your age：')
age = 10
if int(age) > 18:
    print('adult')
else:
    print('teenager')


print('''
-------循环-------
''')

fruits = ['banana', 'apple', 'pineapple', 'peach']
for fruit in fruits:
    print(fruit)

print(list(range(10)))