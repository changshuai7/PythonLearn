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
print(help(str.title))  # 查看某个方法的帮助文档

# 以“__”开头、“__”结尾的方法被约定成私有方法， 不希望被外部直接调用。


# 二、删除空白
# str还提供了如下常用的 方法来删除空白。
# lstrip(): 删除字符串前后的空白。
# rstrip(): 删除字符串前面(左边)的空白。
# rstrip(): 删除字符串后面(右边)的空白。
# 但如果为方法传入指定参数（默认是空格）， 则可删除该字符串左边/右边的指定字符，

# Python 的 str 是不可变的,因此这三个方法只是返回字符串前面或后面空白被删除之后的副 本 ，并没有真正改变字符串本身 。

s_trip = "  test   "
print(s_trip.lstrip())
print(s_trip.rstrip())

s_trip_2 = '88888888i think it is a scarecrow88888888'
print('结果:', s_trip_2.lstrip('8'))

#  二、查找、替换相关的方法。
# str还提供了如下常用的执行 查找 、替换等操作的方法 。
# startswith():判断字符串是否以指定子串开头。
# endswith():判断字符串是否以指定子串结尾 。
# find(): 查找指定子串在字符串中出现的位置，如果没有找到指定子串 ，则返回-1
# index(): 查找指定子串在字符串中出现的位置，如果没有找到指定子串，则引发 ValueError 错误。
# replace(): 使用指定子串替换字符串中的目标子串 。
# translate(): 使用指定的翻译映射表对字符串执行替换。

s_method = 'mty is a good girl'
print(s_method.startswith('m'))
print(s_method.endswith('girl'))
print(s_method.find('a'))
print(s_method.index('m'))
print(s_method.replace('good', 'bad'))

table = {97: 945, 98: 946, 116: 964}
print(s_method.translate(table))

# 三、分割、连接方法
# Python 还为 str 提供了分割和连 接方法 。
# 》 split(): 将字符串按指定分割符分割成多个短语。
# 》 join():  将多个短语连接成字符串。

split_s = "mty is a good girl"
print(split_s.split(" "))
print('/'.join(split_s.split(" ")))
