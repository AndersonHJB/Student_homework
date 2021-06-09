# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 10:12 上午
# @Author  : AI悦创
# @FileName: Animal_class.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创

# x = 0
class Animal(object):
	def __init__(self, name, age):
		self.x = 0
		self.name = name

	def move(self):
		self.x += 10
		return self.x
	
	def l(self):
		print("叫")
		
# 野生程序员
# 专业程序员

dog = Animal(name="旺财", age=19)  # 实例化
cat = Animal(name="大黄", age=18)
# dog.l()
# cat.l()
print(dog.name)
print(cat.name)
