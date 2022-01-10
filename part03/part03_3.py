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

# 与 list()对应的是， Python 也提供了一个 tuple()函数， 该函数可用于将列表、 区间 (range)等对象转换为元组 。
print('\n===================创建元祖===================\n')

print(tuple(range(0, 10, 2)))

# 3.2、增加列表元素

# 为列表增加元素可调用列表的 append()方法，该方法会把传入的参数追加到列表的最后面 。
# append()方法既可接收单个值，也可接收元组、列表等 ，但 该方法只是把元组 、列 表当成单个 元素 ， 这样就会形成在列表中嵌套列表、嵌套元组的情形

print('\n===================列表增加元素===================\n')

list_1 = ['a', 1, 'bcd']
print(list_1)
# 增加元素
list_1.append('hello')
print(list_1)
# 增加元组
list_1.append(tuple(range(5)))
print(list_1)
# 增加列表
list_1.append(['q', 'w', 'e', 'r', 't'])
print(list_1)

#  如果希望不将被追加的列表/元祖当成一个整体，而只是追加列表 中的元素，则可使用列表的 extend()方法。
print('\n')
list_2 = ['a', 1, 'bcd']
print(list_2)
list_2.extend(tuple(range(5)))
print(list_2)
list_2.extend(['q', 'w', 'e', 'r', 't'])
print(list_2)

# 如果希望在列表中间增加元素，则可使用列表的 insert()方法，使用 insert()方法时要指 定将元素插入列表的哪个位置。
print('\n')
list_3 = ['a', 1, 'bcd']
list_3.insert(1, 'insert_data')
print(list_3)
list_3.insert(0, ('a', 'b', 'c'))
print(list_3)

# 3.3、删除列表元素
# 使用 del 语句既可删除列表中的单个元素，也可直接删除列表的中间一段。
print('\n===================列表删除元素===================\n')

list_4 = ['a', 'b', 'c', 'd', 'e']
print(list_4)
del list_4[0]
print(list_4)

print('\n')
list_5 = ['a', 'b', 'c', 'd', 'e']
del list_5[0:5:2]
print(list_5)

print('\n')
my_name = 5
print(my_name)
# 使用 del语句不仅可以删除列表元素，也可以删除普通变量，
del my_name
# print(my_name)  # 会报错 NameError: name 'my_name' is not defined


# 除使用 del语句之外， Python 还提供了 remove()方法来删除列表元素
# 该方法并不是根据索引来删除元素的，而是根据元素本身来执行删除操作的。
# 该方法只删除第一个找到的元素，如果找不到该元素，该方法将会引发 ValueError错误。
print('\n')
list_6 = ['a', 'b', 'c', 'd', 'e']
print(list_6)
list_6.remove('a')
print(list_6)

# 列表还包含一个 clear()方法， 该方法用于清空列表的所有元素。
list_7 = ['a', 'b', 'c', 'd', 'e']
print(list_7)
list_7.clear()
print(list_7)

# 3.4、修改列表元素

# 可以对列表的元素赋值，这样即可修改列表的元素
# 通过索引对列表元素赋值，程序既可使用正数索引，也可使用负数索引
print('\n===================列表修改元素===================\n')

list_8 = ['a', 'b', 'c', 'd', 'e']
list_8[2] = 'cc'
list_8[-2] = 'dd'
print(list_8)
print()

# 程序可通过 slice 语法对列表其中一部分赋值，在执行这个操作时并不要求新赋值的元素个数与原来的元素个数相等。
# 这意味着通过这种方式既可为列表增加元素，也可为列表删除元素。
list_9 = ['a', 'b', 'c', 'd', 'e']
list_9[0:3] = ['aa', 'bb']  # 意味着可以吧c这个元素删除
print(list_9)
# 对列表中空的slice赋值， 就变成了为列表插入元素。
list_9 = ['a', 'b', 'c', 'd', 'e']
# 将第 3 个到第 3 个 (不包含)元素赋值为新列表的元素 ，就是插入元素
list_9[3:3] = ['xxx1', 'xxx2']
print(list_9)
print()

# 如果将列表其中一段赋值为空列表，就变成了从列表中删除元素 。
list_10 = ['a', 'b', 'c', 'd', 'e']
list_10[2:4] = []
print(list_10)
print()

# 对列表使用 slice 语法赋值时，不能使用单个值;
# 如果使用字符串赋值,Python 会自动把字符串当成序列处理，其中每个字符都是一个元素。
list_11 = ['1', '2', '3', '4', '5']
list_11[2:3] = 'hello'
print(list_11)

# 在使用 slice 语法赋值时，也可指定 step 参数
# 但如果指定了 step 参数 ，则要求所赋值的列表元素个数与所替换的列表元素个数相等
list_12 = ['1', '2', '3', '4', '5']
list_12[0:4:2] = ['HELLO', 'WORLD']
print(list_12)

# 3.5 列表的其他常用方法
print('\n===================列表常用方法===================\n')
# 》 count():用于统计列表中某个元素出现的次数。
# 》 index():用于判断某个元素在列表中出现的位置。
# 》 pop():用于将列表当成“技”使用，实现元素出栈功能 。
# 》 reverse():用于将列表中的元素反向存放。
# 》 sort(): 用于对列表元素排序。

# ########### count()
print()
list_13 = ['a', 'b', 'c', 'd', 'e', 'a']
print('a.count=', list_13.count('a'))

# ########### index()

# index():index()方法用于定位某个元素在列表中出现的位置，如果该元素没有出现，则会引发 ValueError错误 。
# 在使用 index()方法时还可传入 start、 end 参数，用于在列表的指定范围内搜索元素。
print()
print('a.index=', list_13.index('a'), '指定范围index', list_13.index('a', 1))

# ########### pop()

# pop()方法用于实现元素出栈功能。战是一种特殊的数据结构，它可实现先入后出(FILO)功 能，即先加入栈的元素，反而后出栈 。
# python没有push方法，我们可以使用 append()方法末代替 push()，实现入栈操作。
# pop()的返回值为出栈的元素
print()
list_14 = ['a', 'b', 'c', 'd', 'e']
print(list_14)
list_14.append('add1')
list_14.append('add2')
print('入栈后列表为', list_14)
print('出栈元素为：', list_14.pop(), '，出栈后结果为', list_14)
print('出栈元素为：', list_14.pop(), '，出栈后结果为', list_14)

# ########### reverse()
print()
list_15 = ['a', 'b', 'c', 'd', 'e']
print('翻转前：', list_15)
list_15.reverse()
print('翻转后：', list_15)

# ########### sort()
print()
list_16 = [100, 20, 6, 50, 45]
print('排序前：', list_16)
list_16.sort()
print('排序后：', list_16)

print()
list_17 = ['good', 'abc', 'hello', 'world', 'dog']
print('排序前：', list_17)
# #对列表元素排序 ， 默认按字符串包含的字符的编码来比较大小
list_17.sort()
print('排序后：', list_17)

# sort()方法除支持默认排序之外，还可传入 key 和 reverse 两个参数，而且这两个参数必须通过参数名指定
# key参数用于为每个元素都生成 一个比较大小的“键”;
# reverse参数则用于执行是否需要反转排序--默认是从小到大排序;如果 将该参数设为 True，将会改为从大到小排序。
print()
list_18 = ['g', 'ab', 'hello', 'pick', 'dog']
print('排序前：', list_18)
list_18.sort(key=len, reverse=True)
print('排序后：', list_18)
