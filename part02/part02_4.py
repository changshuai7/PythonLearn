# coding=utf-8
# 1、字符串

# Python 要求字符串必须使用引号括起来，使用单引号也行 ，使用双引号也行一一只要两边的引号能配对即可。
# Python 3.x对中文字符支持较好，但Python2.x则要求在源程序中增加 # coding=utf-8 ”才能支持中文字符 。

# 如果字符串内容本身包含了单 引号或双引号，此时就需要进行特殊处理 。

# 》使用不同的引号将字符串括起来。
# 》对引号进行转义

str1 = "hello ','  world"  # 双引号可以嵌套单引号,单引号也可以嵌套双引号
print(str1)

str2 = '"hello",world'
print(str2)

str3 = 'hello \' world '  # 通过转义字符转义
print(str3)

# 2、拼接字符串
# 如果直接将两个字符串 紧挨着写在一起，就会自动拼接它们
str4 = "hello" "mty"
str5 = "hello" + "mty"
print("s1=", " ", str4, "\ns2=", " " + str5)

# 3、repr 和字符串
# 有时候， 我们需要将字符串与数值进行拼接， 而 Python 不允许直接拼接数值和字符串 ， 程序 必须先将数值转换成字符串 。
# 为了将数值转换成字符串 ， 可以使用 str()或 repr()函数

# str_ = "mty" + 666 会报错

str6 = "mty" + str(666)
print(str6)

str7 = "mty" + repr(666)
print(str6)

# str本身是 Python 内置的类型(和int、float一样)
# str()函数和repr()函数则只是函数。
# repr还有一个功能， 它会以 Python表达式的形式来表示值。
"""
   返回对象的规范字符串表示形式(返回一个对象的 string 格式。)
   Return the canonical string representation of the object.
   对于许多对象类型，包括大多数内置对象
   For many object types, including most builtins, eval(repr(obj)) == obj.
"""
str8 = "hello mty"
print(str8)
print(repr(str8))

obj = {'key1': 'value1', 'key2': 'value2'}
print(obj)
print(repr(obj))

# 在交互式解释器中输入一个主量或表达式时， Python会自动使用 repr()函数处理该变量或表达式 。

# 4、使用 input 和 raw_input 获取用户输入
# input()函数用于向用户生成一条提示，然后获取用户输入的内容。
# 由于 input()函数总会将用户 输入的内容放入字符串中，因此用户可以输入任何内容， input()函数总是返回一个字符串。

"""
# 演示的时候放开
input_start = input('\n\n请输入:\n')
print("输入结果为", input_start, ",类型为", type(input_start))
"""
# 无论输入哪种内容，始终可以看到 input()函数返回字符

# 需要指出的是， Python2.x提供了一个 raw input()函数，该 raw_input()函数就相当于 Python3.x中的 input()函数。
# 该 input()函数则比较怪异:要求用户输入的必须是符合 Python 语法的表达式。
# 通常来说，用户只能输入整数、浮点数、复数、字符串等。重点是格式 必须正确，比如输入字符串时必须使用双引号

# 输入  2  ==> <class 'int>
# 输入 "2" ==> <class 'str'>
# 输入 hello => 报错

# 5、长字符串

# 注释时提到使用 三个引号(单引号、双引号都行)来包含多行注释内容， 其实这是长字符串写法
# 只是由于在长字符串中可以放置任何内容，包括放置单引号、双引号都可以，
# 如果所定义的长字符串没有赋值给任何变量，那么这个字符串就相当于被解释器忽略了，也就 相当于注释掉了。
# 这种形式非常 强大，可以让字符串中包含任何内容，既可包含单引号，也可包含双引号 。
'''
hello mty
'''

long_str1 = """
hello 
    mty 
    you are a good "girl"
"""

long_str2 = '''
hello 
    mty
    'you are a good "girl'
'''

print(long_str1)
print(long_str2)

# 此外， Python 还允许使用转义字符(\〉 对换行符进行转义，转义之后的换行符不会“中断” 字符串 。 例如如下代码(程序清单同上) 0

long_str3 = 'hello mty1\
    mty2\
    mty3'
print(long_str3)

#  Python 程序的换行、缩进都有其规定的语法。所以， Python 的表达式不允许随便换行。
#  如果程序需要对 Python 表达式换行，同样需要使用 转义字符( \)进行转义，代码如下:
result = 3 * 5 + \
         2 * 5
print(result)


# 6、原始字符串
# 由于字符串中的反斜线都有特殊的作用，因此当宇符串中包含反斜线时，就需要对其进行转义

# 比如一个目录路径：'C:\python\codes\02\2.4'
# 使用该路径值，需要写成：'C:\\python\\codes\\02\\2.4'
# 此时可借助于原始宇符串来解决这个 问题 。
# 原始字符串以“ r”开头 ， 原始宇符串不会把反斜线当成特殊字符。因此，上面的 Windows 路 径可直接写成 r' C:\python\codes\02\2.4’。
src_str1 = r'C:\python\codes\02\2.4'
print(src_str1)

src_str2 = r'"Let\'s go" world'
print(src_str2)


# 7、字节串
# Python 3 新增 了 bytes 类型 ，用于代表字节串。
# 宇符串(str)由多个字符组成， 以字符为单位进行操作 ;
# 字节串(bytes)由多个字节组成，以字节为单位进行操作 ;
# bytes 和 str 除操作的数据单元不同之外，它们支持的所有方法都基本相同，
# bytes 对象只负责以宇节(二进制格式)序列来记录数据
# bytes 保存的就是原始的字节( 二进制格式)数据，因此 bytes 对象可用于在网络上传输 数据 ，也可用于存储 各种二进制格式的文件， 比如 图片/音乐

# 字符 -> 转 -> 字节
# 方式1：字符串之前添加 b 来构建字节串值（要求：必须内容都是 ASCII 字符）
# 方式2：调用 bytes()构造方法
# 方式3：调用 字符串本身 的 encode()方法将字符串按指定宇符集转换成字节串，如果不指定字符集，默认使用 UTF-8字符集。
# 输出结果：16进制值 比如：\xe5\xa5\xbd

b1 = bytes('好', encoding= 'utf-8')
# b2 = b'好' # 报错
b2 = b'hello'

b3 = '好'.encode('utf-8')
print(b1)
print(b2)
print(b3)


# 字节串和字符串非常相似，只是字节串里的每个数据单元都是1个字节（8bit）
# ASCII -> 8位，1 字节(支持 256 个字符编号)
# Unicode字符集 ->16位，2个字节（支持65536个字符编号）
#     -衍生UTF-8,
#     -衍生UTF-16,









