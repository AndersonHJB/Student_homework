name=input('请入输您的姓名：')
gender=input('请入输您的性别：')
school=input('请入输您的学校：')

print('*'*30)
print('\n\t\t简历\n')
print('姓名：{}'.format(name))
print('性别：{}'.format(gender))
print('学校：{}'.format(school))
print('*'*30)

# 整体来说，思路清晰从输入到输出整体给出的代码清晰。
#但，对于之后的多人协作完成某个项目，就需要更加清晰快速定位，所以我们需要做出如下几点优化：
# 1.划分区域；
# 2.变量名再更加直观一些；
# 3.为了使代码更具有观赏性，建议：在赋值号两边加上空格；
# 4.星号的优化；（你已经做到了）
# 6.在print当中，能不掉用函数尽量不调用，为了提升代码运行效率；
# 7.简历内容可以更加完善；
# 扩展可以添加一个动态效果，在这里我就不讲述，自己有兴趣去查找一下；
# 注意：文件命名不要用“-”要用这个："_":就是这样命名：my_report.py

#修改demo：
# 1.划分区域：
#<----------------user_input_area--------------->
name = input('请入输您的姓名：')
gender = input('请入输您的性别：')
school = input('请入输您的学校：')

#<----------------print_area--------------->
print('*'*30)
print('\n\t\t简历\n')
print('姓名：{}'.format(name))
print('性别：{}'.format(gender))
print('学校：{}'.format(school))
print('*'*30)
# 2.变量名再更加直观一些:
# 因为有时候输入的内容很多，你得区分哪些是系统输入变量，哪些是人工输入变量。
# 英文版：(Because sometimes there is a lot of input, you have to distinguish between system input variables and manual input variables.)
# 修改示例：在变量前面加个user即可(并尽量用英文）；
user_name = input('请入输您的姓名：')
user_gender = input('请入输您的性别：')
user_school = input('请入输您的学校：')

# 3.为了使代码更具有观赏性，建议：在赋值号两边加上空格；
# 修改示例：
user_name = input('请入输您的姓名：')
user_gender = input('请入输您的性别：')
user_school = input('请入输您的学校：')
# 4.星号的优化:
#多个星号这样输出：(你已经做到）
print('*'*30)  # 数字30就是你要几个星号；

# 6.在print当中，能不掉用函数尽量不调用，为了提升代码运行效率；
#修改示例：
print('*'*30)
print('\t简历')
print('姓名:'user_name)
print('性别:'user_gender)
print('学校:'user_school)

# 7.简历内容可以更加完善；
# 例如这样（简单示例）：
#<----------------user_input_area--------------->
name = input('请输入您的姓名：')
gender = input('请输入您的性别：')
age = input('请输入您的年龄：')
university = input('请输入您的学校：')
address = input('请输入您的住址：')
#<----------------print_area--------------->
print('正在生成您的简历......')
print('******************************')
print('             简历      ')
print(name1+name)
print(xingbie1+xingbie)
print(age1+age)
print(school1+school)
print('over thanks')

    
# 好整体就是这样，希望下次看见你的代码有所提升哦，一起加油吧！