# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 9:59 上午
# @Author  : AI悦创
# @FileName: move_demo.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
dog_x = 0
cat_x = 0


def dog_move():
	global dog_x
	dog_x += 10
	# print(dog_x)
	return dog_x

def cat_move():
	global cat_x
	cat_x += 10
	# print(cat_x)
	return cat_x
	

user_input = "move"
if __name__ == '__main__':
	# print("aaa")
	if user_input == "move":
		print("dog:{}, cat:{}".format(dog_x, cat_x))
		dog_move()
		cat_move()
		print("dog:{}, cat:{}".format(dog_x, cat_x))
		print("dog:{}, cat:{}".format(dog_move(), cat_move()))