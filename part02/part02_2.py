# coding=utf-8
# 1、变量的命名规则

# 必须以字母、下画线(_)开头， 后面可以跟任意数目的字母、数字和下画线(_)
# Python3.x 支持 UTF-8 字符集，因此 Python 3 的标识符可以使用 UTF-8 所能 表示的多种语言的宇符
# python2.x 对中文支持较差，如果要在Python2.x程序中使用中文字剧中文变量，
# 则需要在 Python 源程序的第一行增加"# coding=utf-8"
# 同时源文件也要保存为"UTF-8"字符集

# 标识符可以由字母、数字、下画线()组成，其中数字不能打头 。
# 标识符不能是 Python 关键字，但可以包含关键字。
# 标识符不能包含空格.


# 2、Python 的关键字和内置函数

# Python还包含一系列关键字和内置函数 ， 一般也不建议使用它们作为变量名 。
# 如果开发者尝试使用关键字作为变量名 ， Python解释器会报错。（比如and/as/if/else）
# 如果开发者使用内置函数的名字作为变量名， Python解释器倒不会报错，只是该内置函数就被这个变量覆盖了，该内置函数就不能使用了 。（比如 any()/abs()）



