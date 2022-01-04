# coding=utf-8


"""
三、使用列表
"""

# 列表与元组最大的区别在于:元组是不可改变的，列表是可改变的

# 3.1、创建列表

# Python 还提供了一个内置的list()函数来创建列表； list()函数可用于将元组、区间(range)等对象转换为列表。

print('\n===================创建列表===================\n')

list_a = list(('a', 1, 'test'))
print(list_a)

list_b = list(['b', 12, 'test'])
print(list_b)

list_c = list(range(3, 20, 5))
print(list_c)  # 3/8/13/18

# Python 2.x提供了一个xrange()函数，与Python3.x中中的range()函数基本相同。
# Python 2.x也提供了 range()函数，但是该函数返回的是列表对象

