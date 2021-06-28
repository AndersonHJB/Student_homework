# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 4:44 下午
# @Author  : AI悦创
# @FileName: demo01.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
def sum_digits(y):
	sum_value = 0
	str_y = str(y)
	for num in str_y:
		sum_value = sum_value + int(num)
	return sum_value

if __name__ == '__main__':
	print(sum_digits(4224))