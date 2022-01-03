# coding=utf-8

# 一、序列相关方法

# 字符串本质上就是由多个字符组成的，因此程序允许通过索引来操作字符， 比如获取指定索引 处的字符，获取指定字符在字符串中的位置等 。

# Python字符串直接在方括号([])中使用索引即可获取对应的字符

s = 'mty'
print(s[0], '-', s[1], '-', s[2])

# 除可获取单个字符之外，也可在方括号中使用范围来获取字符串的中间“一段”(被称为子串）
# 特点：包前不包后；起始索引、结束索引可省略
print(s[0:2])
print(s[0:])
print(s[:3])
print(s[:])

# python 字符串 还支持用 in 运算符判断是否包含某个子串。

print('m' in s)

# 如果要获取字符串的长度，则可调用 Python 内置的 len()函

print(len(s))

# 还可使用全局内置的 min()和 max()函数获取字符串中最小字符和最大字符。
print('最大字符：', max(s))
print('最小字符：', min(s))

# Python 是“自带文档”的;常用的两个帮助函数
# dir(): 列出指定类或模块包含的全部内容(包括函数、方法、类、变量等)。
# help(): 查看某个函数或方法的帮助文档。

# 以str()方法为例
print(dir(str))
# print(help(str))
print(help(str.title)) # 查看某个方法的帮助文档

# 以“__”开头、“__”结尾的方法被约定成私有方法， 不希望被外部直接调用。


# 二、删除空白
# str还提供了如下常用的 方法来删除空白。
# lstrip(): 删除字符串前后的空白。
# rstrip(): 删除字符串前面(左边)的空白。
# rstrip(): 删除字符串后面(右边)的空白。
# 但如果为方法传入指定参数， 则可删除该字符串左边/右边的指定字符

# Python 的 str 是不可变的,因此这三个方法只是返回字符串前面或后面空白被删除之后的副 本 ，并没有真正改变字符串本身 。

s_trip = "  test   "
print(s_trip.lstrip())
print(s_trip.rstrip())

# TODO 这里不太理解 P32页，删除字符串前后指定字符
s_trip_2 = 'i think it is a scarecrow'
print('结果:', s_trip_2.lstrip('i'))