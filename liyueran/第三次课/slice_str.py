# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 11:00 上午
# @Author  : AI悦创
# @FileName: slice_str.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
str_name = "aiyuechuang"
print(str_name[10])
print(str_name[len(str_name) - 1])
print(str_name[-1])

# """aiyu"""
print(str_name[0:4])
# """huang"""
print(str_name[6:len(str_name)])
print(str_name[6:12])

# """6:"""
print(str_name[6:len(str_name)])
print(str_name[6:])
print(str_name[:6])

# aiyuechuang
# a y e h a g
print(str_name[::2])

print(str_name[1::2])
print(str_name[6:3:-1])


str_name.replace()
