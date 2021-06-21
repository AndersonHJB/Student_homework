username_iphone = ['aiyc', 123, 'lilei', 520, 'hanmeimei', 131]
try:
	print(username_iphone[username_iphone.index("aiyc2020")])
except ValueError as e:
	print(e)