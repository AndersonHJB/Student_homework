"""
# -*- coding: utf-8 -*-
# @Author：AI悦创 @DateTime ：2019/9/29  21:46 @Function ：功能  Development_tool ：PyCharm
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import random
user_genter = input('性别')
user_age = int(input('年龄'))

if user_age < 18:
	lucky = ('考试满分')
	unlucky = ('考试发挥失常')
	print(random.choice([lucky,unlucky]))
elif int(user_age) >= 18:
	lucky = '开心'
	unlucky = '不开心'
	print(random.choice([lucky,unlucky]))
#
# user_input = input("Please you in input:>>>")
# input_type = type(user_input)
# input_type_int = type(int(user_input))
# print(f'input type is {input_type}')
# print(f'input type_int is {input_type_int}')


