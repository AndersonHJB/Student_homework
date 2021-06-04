import time

a = False

#姓名输入
user_name = input('请输入你的姓名： ')

#性别输入
while not a:
	user_gender = input('请输入你的性别(男/女）： ')
	if user_gender == '男' or user_gender == '女':
		break
	else:
		print('请正确输入你的性别')
		continue

#年龄输入
while not a:
	user_age=input('请输入你的年龄： ')
	if user_age.isdigit() and int(user_age) <= 120:
		break
	else:
		print('请正确输入你的年龄')
		continue

#运势生成
print('正在生成中......')
time.sleep(1)
print('')
print('*'*3+user_name+'今年的运势'+'*'*3)
print('你会考上清华并且找到一个对象')

# 整体来看，完成的效果不错！
# 但有以下几点建议：
# 1.在简历代码作业中，我已经提出代码划分区域，看你代码一共有三个while循环，何不放在同一个区域呢？
# 简单示例：
#<----------------------while_area------------------->
#性别输入
while not a:
	user_gender = input('请输入你的性别(男/女）： ')
	if user_gender == '男' or user_gender == '女':
		break
	else:
		print('请正确输入你的性别')
		continue

#年龄输入
while not a:
	user_age=input('请输入你的年龄： ')
	if user_age.isdigit() and int(user_age) <= 120:
		break
	else:
		print('请正确输入你的年龄')
		continue

        
        
# 2.不知道你有没有发现你所写的两个while循环所到达的或者说形式差不多，为何不把他用函数封装起来呢？（作为扩展，不做示例）

# 3.初步达到动态效果不错。(可以试一试把原先用户输入的界面清空，不做示例）
# 4.臃肿：
a = False
while not a:
    pass

# 这样写会更好：
while True:
    pass
