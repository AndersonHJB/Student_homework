# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 9:18 上午
# @Author  : AI悦创
# @FileName: def_fun02.py.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创

def HelloUser(username=None, age=None):
	result = "hello {}, age: {}".format(username, age)
	# print(result)
	return result

a = HelloUser(age=18, username="aiyc")
print(a)

str1 = "aiyc"
a = str1.replace("a", "lll")
# print(a)