user_input_gender = input("请输入你的性别（F/M）")
user_input_age = input（"请输入你的年龄(0-100)"）  
if user_input_gender == F and  0 <user_input_age<=20:  
	print("你会考上清华找一个白马王子")
elif user_input_gender == F and  20 <user_input_age<=50:
	print("你会变为天底下最漂亮的女富婆")
elif user_input_gender == F and  50 <user_input_age<=100:
	print("你会变为长寿的老奶奶")
#女孩
elif user_input_gender == M and  0 <user_input_age<=20:
	print("你会考上清华找一个白雪公主")
elif user_input_gender == M and  20 <user_input_age<=50:
	print("你会变成事业有成的高富帅")
elif user_input_gender == M and  50 <user_input_age<=100:
	print("你会变为快乐的老爷爷")
#男孩
elif user_input_gender not (M or F):
	print("性别只能是F或者M")
elif user_input_age>100 or user_input_age<0:
	print("年龄范围不对哦")
else
	print("输入错误请重新输入")
#错误

# 由代码整体来看，整体的逻辑表现完成的不错；
# 1.注意input输入得到的数据类型是str（字符串类型）>>>不懂的话可以用type检测，我脑图里面也有相应的示例！！！
# 2.在代码中，全部都要在英文输入法下输入，除了中文。
# 3.看你得代码是及时性的回复运势推演结果，但我们能不能先统一获取用户(User)信息，再输出会不会更好，用户体验效果会更好呢？
# 4.按你现在的代码，当用户(User)输入错误的时候，并不能达到让程序自动等用户输入正确。你现在的结果就是，用户输入错误，程序也就停止运行，咱们能不能考虑加个循环呢？（不做示例，独立思考！）
# 请将代码块分区，分成输入区、输出区、循环区等等，简历的代码中已经提出这个意见，希望认真看完后做出修改！！！（不做示例）




# 2.在代码中，全部都要在英文输入法下输入，除了中文。
# 你这段代码用的是中文括号，以后要注意!
user_input_age = input（"请输入你的年龄(0-100)"）  







