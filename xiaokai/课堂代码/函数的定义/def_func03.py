# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 9:25 上午
# @Author  : AI悦创
# @FileName: def_func03.py.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创



def HelloUser(username=None, age=None):
	lst = []
	a = 10000
	lst.append(username)
	lst.append(age)
	return (lst, a)

# print(result)

# lst, a1 = HelloUser(age=18, username="aiyc")
t = HelloUser(age=18, username="aiyc")
print(t)
