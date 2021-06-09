# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 9:40 上午
# @Author  : AI悦创
# @FileName: demo.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
a = 1
# global

def hello():
	global a
	a += 1
	print(a)


hello()
print(a)
