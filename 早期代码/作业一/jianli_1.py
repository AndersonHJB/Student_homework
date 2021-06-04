name=input("请输入您的姓名：")
gender=input("请输入您的性别：")
university=input('请输入您的学校：')
age=input('请输入您的年龄：')
print('*'*30)
print('\n\t\t简历\n')
print('姓名:{}'.format(name))
print('性别:{}'.format(gender))
print('学校：{}'.format(university))
print('年龄:{}'.format(age))
print('*'*30)

# 整体来说，思路清晰从输入到输出整体给出的代码清晰。
#但，对于之后的多人协作完成某个项目，就需要更加清晰快速定位，所以我们需要做出如下几点优化：
# 1.划分区域；
# 2.变量名再更加直观一些；
# 3.在print当中，能不掉用函数尽量不调用，为了提升代码运行效率；
# 4.为了使代码更具有观赏性，建议：在赋值号两边加上空格；
# 扩展可以添加一个动态效果，在这里我就不讲述，自己有兴趣去查找一下；

#修改demo：
# 1.划分区域：
#		#<----------------user_input_area--------------->
		name=input("请输入您的姓名：")
		gender=input("请输入您的性别：")
		university=input('请输入您的学校：')
		age=input('请输入您的年龄：')

#		#<----------------print_area--------------->
		print('*'*30)
		print('\n\t\t简历\n')
		print('姓名:{}'.format(name))
		print('性别:{}'.format(gender))
		print('学校：{}'.format(university))
		print('年龄:{}'.format(age))
		print('*'*30)
        
# 2.变量名再更加直观一些:
# 因为有时候输入的内容很多，你得区分哪些是系统输入变量，哪些是人工输入变量。
# 英文版：(Because sometimes there is a lot of input, you have to distinguish between system input variables and manual input variables.)
# 修改示例：在变量前面加个user即可；
		user_name=input("请输入您的姓名：")
		user_gender=input("请输入您的性别：")
		user_university=input('请输入您的学校：')
		user_age=input('请输入您的年龄：')
    
# 3.在print当中，能不掉用函数尽量不调用，为了提升代码运行效率；
#修改示例：
		print('*'*30)
		print('\n\t\t简历\n')
		print('姓名:'user_name)
		print('性别:'user_gender)
		print('学校:'user_university)
		print('年龄:'user_age)
		print('*'*30)

# 4.为了使代码更具有观赏性，建议：在赋值号两边加上空格；
# 修改示例：
		user_name = input("请输入您的姓名：")
		user_gender = input("请输入您的性别：")
		user_university = input('请输入您的学校：')
		user_age = input('请输入您的年龄：')
    
# 好整体就是这样，希望下次看见你的代码有所提升哦，一起加油吧！