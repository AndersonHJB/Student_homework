# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 3:44 下午
# @Author  : AI悦创
# @FileName: demo.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
# 统计词频
words_list = []
words_dict = {}
with open("i_have_a_dream.txt", "r", encoding="utf-8") as f:
	lines = f.readlines()
	# print(lines)
	for line in lines:
		line = line.replace(",", "")
		line = line.replace(".", "")
		line = line.replace("?", "")
		line = line.replace("!", "")
		line = line.replace(":", "")
		line = line.replace("\n", "")
		line = line.replace("", "")
		# print(line)
		words = line.split(" ")
		for word in words:
			if word:
				words_list.append(word)

for word in words_list:
	if word in words_dict:
		words_dict[word] += 1
	else:
		words_dict[word] = 1
print(words_dict)
# print(len(words_list))
# t = set(words_list)
# print(t)
# print(len(t))
