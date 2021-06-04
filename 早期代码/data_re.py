# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author：AI悦创 @DateTime ：2019/11/13 21:24 @Function ：功能  Development_tool ：PyCharm
# code is far away from bugs with the god animal protecting
#    I love animals. They taste delicious.
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
# print(result)# 输出匹配结果
print(result.group())# 获取匹配的内容（匹配的结果）
print(result.span())# 获取匹配的长度