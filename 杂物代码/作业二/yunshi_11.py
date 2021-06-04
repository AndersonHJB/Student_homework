print("    请输入以下信息测试您今年的运势~~")
print("*"*20)

user_name=input("您的名字:")

user_gender_correct=False
while not user_gender_correct:
	user_gender=input("您的性别（男/女）：")
	if user_gender=="男":
		user_gender_correct=True
	elif user_gender=="女":
	    user_gender_correct=True
	else:
		print("请正确输入您的性别（男/女）")

user_birthyear=input("您的出生年份：")

user_sign_correct=False
while not user_sign_correct:
    user_sign=input("您的生肖（鼠/牛/虎/兔/龙/蛇/马/羊/猴/鸡/狗/猪）：")
    if user_sign == "鼠":
        print("***\n经过分析，您今年將会：\n   在逛街时偶遇周杰伦并成功要到签名")
        user_sign_correct=True
    elif user_sign == "牛":
        print("***\n经过分析，您今年將会：\n   在无意中发现祖宗留下的宝藏")
        user_sign_correct=True
    elif user_sign == "虎":
        print("***\n经过分析，您今年將会：\n   在学业上比较平稳且顺畅")
        user_sign_correct=True
    elif user_sign == "兔":
        print("***\n经过分析，您今年將会：\n   成功牵到TA的手，走上人生巅峰")
        user_sign_correct=True
    elif user_sign == "龙":
        print("***\n经过分析，您今年將会：\n   遇到一些小麻烦但最终都会顺利解决")
        user_sign_correct=True
    elif user_sign == "蛇":
        print("***\n经过分析，您今年將会：\n   实现一个长久以来的心愿")
        user_sign_correct=True
    elif user_sign == "马":
        print("***\n经过分析，您今年將会：\n   考上理想的大学")
        user_sign_correct=True
    elif user_sign == "羊":
        print("***\n经过分析，您今年將会：\n   发现自己未知的天赋")
        user_sign_correct=True
    elif user_sign == "猴":
        print("***\n经过分析，您今年將会：\n   平稳却平淡地度过")
        user_sign_correct=True
    elif user_sign == "鸡":
        print("***\n经过分析，您今年將会：\n   中1000万彩票大奖，走上人生巅峰")
        user_sign_correct=True
    elif user_sign == "狗":
        print("***\n经过分析，您今年將会：\n   获得周围的人的高度认可和欢迎")
        user_sign_correct=True
    elif user_sign == "猪":
        print("***\n经过分析，您今年將会：\n   得到一份更好的工作")
        user_sign_correct=True
    else:
        print("请正确输入您的生肖~~")

print("*"*20)
print("      感谢您的使用，祝您好运~")


# 整体做的不错，逻辑清晰；
#  提出几点优化：
# 1.已经做到while循环，赋值符号直接加空格：
user_name = input("您的名字:")

# 2.有没有想过吧这些输出的数据做成字典的数据类型呢？把生效做出key，把对应的做出value（扩展）
# 类似这样的：
dict1 = {"鼠": "在逛街时偶遇周杰伦并成功要到签名", "牛":"在无意中发现祖宗留下的宝藏"}

# 这个部分用就是字符串不要用空格用\t
print("\t\t\t感谢您的使用，祝您好运~")
# 加油吧！
# 代码划区域作业已经讲过了，注意看并修改）