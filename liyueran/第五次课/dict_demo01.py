# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 9:01 上午
# @Author  : AI悦创
# @FileName: dict_demo01.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
# 电话本
# 用户名称：手机号
# list/tuple >>> list
username = ['aiyc', 'lilei', 'hanmeimei']
iphone_numbers = [124, 520, 131]
# 我要查询：aiyc 电话号码
# name = input("Please your name:>>>")
name = "aiyc"
try:
	print(iphone_numbers[username.index(name)])
except:
	print(f"未查询到：{name}")