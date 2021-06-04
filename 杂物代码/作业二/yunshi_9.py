def horoscope():
	print("*****星座运势*****")
while True:
	try:       								
		user_gender = input("请输入您的性别（F/M）:")
		user_age = int(input("请输入你的年龄（0~100）："))

		if user_gender =="F":
			if 0< user_age <= 100:
				horoscope()
				print("你将拥有男朋友\n")
			else:
				print("\n请输入符合要求的年龄！\n")
		elif user_gender =="M":
			if 0 < user_age <= 100:
				horoscope()
				print("你将拥有女朋友\n")
			else:
				print("\n请输入符合要求的年龄！\n")
		else:
			print("\n请输入正确的性别F/M\n")	
	except Exception as e:
		print("\nerror!请输入符合规范的内容！\n")
        
# 整体来说代码不错，逻辑清晰。
# 在作业二中达到了我的要求：函数封装、循环、还引用了try----except的异常处理；
# 运势内容可以再完善一些，可以把运势推算的内容建成一个字典存放，那样的效果会更好，代码更简洁：
# 示例：
# key位：年龄,value位：相应的运势（可以是其他的）
luck = {'18':'清华大学', '20':'前程似锦'} # 等等这样代码块就可以分区，分区作业一有讲，这里不再重复。

#函数封装过于简单，可以尝试把输入与循环分开（此为扩展，不做示例）




