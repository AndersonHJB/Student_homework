# -*- coding: utf-8 -*-
# @Time    : 2021/6/25 3:44 下午
# @Author  : AI悦创
# @FileName: demo4.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
class Animal():
	def __init__(self):
		# print("眼睛、嘴巴")
		self.x = 0
	def move(self):
		self.x += 10
		# return self.x
		print(self.x)

if __name__ == '__main__':
	dog = Animal()
	cat = Animal()
	print(dog.move())
	# print(dog.x)
	print(cat.move())
	# print(cat.x)