#! /usr/bin/python
# -*- coding: utf8 -*-

# 字符串转义 \, r
print('i\'am htzhu')

# r'' 内部不做转义
print(r'\\')

# 使用 '''...''' 代替 \n 换行
print('''abc
def
hij
''')

# 布尔值 True False
print(True, False)

# and、or、not
print(True and False)
print(True or False)
print(not False)

# if
if 1 > 0:
    print('oh my god')
else:
    print('yes')

# 变量
age = 10
name = 'htzhu'
salary = 10.10
print(age + 10, name * 2, salary)

# 占位符
print('hello %s, %d, %f' % ('htzhu', 20, 10.10))
# %s 会把任何数据类型转换为字符串
print('hello %s, %s, %s' % ('htzhu', 20, 10.10))
# %% 转义 表示一个%
print('%d %%' % 22)

