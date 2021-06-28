# -*- coding: utf-8 -*-
# @Time    : 2021/6/25 3:37 下午
# @Author  : AI悦创
# @FileName: demo3.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
dog_x = 0
cat_x = 0

def dog_move():
	global dog_x
	dog_x += 10
	return dog_x
	
def cat_move():
	global cat_x
	cat_x += 10
	return cat_x

if __name__ == '__main__':
	dog_move()
	print("dog_move:", dog_x)
	cat_move()
	print("cat_move:", cat_x)