# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 10:51 上午
# @Author  : AI悦创
# @FileName: str_demo.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
str_text = '''
可以随时修改变量，比如把 name 改成 'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的 'Bill' 存储到磁盘上，下次重新运行程序，变量又被初始化为 'Bob'。
​

我们把变量从内存中变成可存储或传输的过程称之为序列化，在 Python 中叫 pickling，在其他语言中也被称之为 serialization，marshalling，flattening 等等，都是一个意思。
​

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
'''
print(str_text)
# \n = new line