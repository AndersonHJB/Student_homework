# !/usr/bin/python3
# -*- coding: utf-8 -*-
# s = ','
# for n in range(0, 10):
#     s += str(n)
# print(s)
#
#
#
#
# l = []
# for n in range(0, 100000):
#     l.append(str(n))
# l = ','.join('lsdscdfsdg')
# print(l)
A = ['x', 'y']
b = [1, 2]
# for i in A:
# 	for n in b:
# 		print(f'{i}={n}')
# # print("{}={}".format(i,n))
print(zip(A, b))
for i in zip(A, b):
	print(i)
	str_1 = f'{i[0]}={i[1]}'
	print(str_1)
# list_1 = ['{i}={n}'.format(i = i, n = n) for i in A for n in b]
# print(list_1)