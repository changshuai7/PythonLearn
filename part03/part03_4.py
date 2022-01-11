# coding=utf-8
"""
四、使用字典
"""

# 4.1、创建字典

# 程序既可使用花括号语法来创建字典，也可使用 dict()函数来创建字典。实际上dict 是一种 类型，它就是 Python 中的字典类型 。
# 字典的key，必须是不可变类型的。
# 字典相当于索引是任意不可变类型的列表:而列表则相当于 key 只能是整数的字典。

print('\n===================创建字典===================\n')

dict_1 = {'语文': 90, '数学': 80, '英语': 100}
dict_2 = {}
# 注意：元组可以作为dict的 key，但列表不能作为元组的key
# 这是由于 dict要求 key 必须是不可变类型，但列表是可变类型.
dict_3 = {('a', 'b'): 'hello world'}

# 在使用 dict()函数创建字典时 ，可以传入多个列表或元组参数作为 key-value对，
# 每个列表或元组将被当成一个key-value 对，因此这些列表或元组都只能包含两个元素。

list_temp = [('a', 1), ('b', 2), ['c', 3]]
dict_5 = dict(list_temp)
print(dict_5)

# 如果不为 dict()函数传入任何参数，则代表创建一个空的字典。
dict_6 = dict()
print(dict_6)

# 还可通过为 dict指定关键字参数创建字典，此时字典的 key不允许使用表达式。
dict_7 = dict(name='mty', age=12)
print(dict_7)

# 4.2、字典的基本用法
print('\n===================字典的基本用法===================\n')

# 全部基于key来操作

dict_8 = {'a': 1, 'b': 2, 'c': 3}
# ①通过key访问value
print(dict_8['a'])

# ②为dict添加 key-value对，只需为不存在的 key赋值即可
dict_8['d'] = 4
print(dict_8)

# ③删除宇典中的 key-value 对，则可使用 del 语句。
del dict_8['a']
print(dict_8)

# ④给字典中的 value重新赋值
dict_8['d'] = 444
print(dict_8)

# ⑤ 如果要判断字典是否包含指定的 key，
print('d' in dict_8, 'ddd' in dict_8)
print('d' not in dict_8, 'ddd' not in dict_8)

# 4.3、字典的常用方法
print('\n===================字典的常用用法===================\n')

# 方法：clear()   =>  用于清空宇典中所有的 key-value 对，空字典
print()
dict_9 = {'a': 1, 'b': 2, 'c': 3}
print(dict_9)
dict_9.clear()
print(dict_9)

# 方法：get()    => 根据 key 来获取 value

# get()方法 它相当于方括号语法的增强版
# 使用方括号语 法访问并不存在的 key时，字典会引发 KeyError错误。
# 使用 get()方法访问不存在的 key, 该方法会简单地返回 None，不会导致错误。

print()
dict_10 = {'a': 1, 'b': 2, 'c': 3}
# print(dict_10['d'])  # 报错 KeyError: 'd'
print(dict_10.get('d'))  # 返回None

# 方法：update()  => 使用一个字典所包含的 key-value对，来更新己有的字典

# 如果被更新的字典中己包含对应的 key-value 对， 那么原 value 会被覆盖。
# 如果被更新的字典中不包含对应的 key-value对， 则该 key-value对被添加进去。

print()
dict_11 = {'a': 1, 'b': 2, 'c': 3}
dict_11.update({'a': 111})  # 更新元素
dict_11.update({'d': 4})  # 增加元素
print(dict_11)

# 方法：items()、 keys()、 values()分别用于 获取字典 中的所有 key-value对、所有key、所有value。

# 这 三个方法依次返回 dict_items、 dict_keys和 dict_values对象，
# Python 不希望用户直接操作这几个方法，但可通过 list()函数把它们转换成列表
print()
dict_12 = {'a': 1, 'b': 2, 'c': 3}
print(dict_12.items())
print(dict_12.keys())
print(dict_12.values())
print()
print(list(dict_12.items()))
print(list(dict_12.keys()))
print(list(dict_12.values()))

# 方法：pop()   ==>  pop()方法用于获取指定 key 对应的 value，并删除这个 key-value对
print()
dict_13 = {'a': 1, 'b': 2, 'c': 3}
print(dict_13.pop('a'))
print(dict_13)

# 方法：popitem()  ==>  弹出字典中最后一个 key-value 对

# 由于字典存储 key-value 对的顺序是不可知的，因此开发者感觉字典的 popitem()方法是“随机”弹出的
# 但实际上字典的 popitem()方法总是弹出底层存储的最后 一个 key-value 对。
# popitem弹出的就是一个元组
print()
list_14 = {'a': 1, 'b': 2, 'c': 3, 'e': 5, 'd': 4}
list_14.update({'f': 6})
x, y = list_14.popitem()  # 序列解包
print('x=', x, 'y=', y)
print(list_14)
