name=input('请输入您的姓名:')
xingbie=input('请输入您的性别:')
age=input('请输入您的年龄:')
school=input('请输入您的学校:')
name1='姓名:'
xingbie1='性别:'
age1='年龄:'
school1='学校:'
kongge=input()
print('正在生成您的简历......')
kongge1=input()  #这是做什么的？
print('******************************')
print('             简历      ')

print(name1+name)
print(xingbie1+xingbie)
print(age1+age)
print(school1+school)


print('over thanks')


# 整体来说，思路清晰从输入到输出整体给出的代码清晰。
#但，对于之后的多人协作完成某个项目，就需要更加清晰快速定位，所以我们需要做出如下几点优化：
# 1.划分区域；
# 2.变量名再更加直观一些；
# 3.为了使代码更具有观赏性，建议：在赋值号两边加上空格；
# 4.星号的优化；
# 5.部分多余代码；
# 6.输出修改
# 扩展可以添加一个动态效果，在这里我就不讲述，自己有兴趣去查找一下；

#修改demo：
# 1.划分区域：
#<----------------user_input_area--------------->
name=input('请输入您的姓名:')
xingbie=input('请输入您的性别:')
age=input('请输入您的年龄:')
school=input('请输入您的学校:')

#<----------------print_area--------------->
print('正在生成您的简历......')
print('******************************')
print('             简历      ')
print(name1+name)
print(xingbie1+xingbie)
print(age1+age)
print(school1+school)
print('over thanks')
# 2.变量名再更加直观一些:
# 因为有时候输入的内容很多，你得区分哪些是系统输入变量，哪些是人工输入变量。
# 英文版：(Because sometimes there is a lot of input, you have to distinguish between system input variables and manual input variables.)
# 修改示例：在变量前面加个user即可(并尽量用英文）；
user_name = input('请输入您的姓名:')
user_sex = input('请输入您的性别:')
user_age = input('请输入您的年龄:')
user_school = input('请输入您的学校:')


# 3.为了使代码更具有观赏性，建议：在赋值号两边加上空格；
# 修改示例：
user_name = input('请输入您的姓名:')
user_sex = input('请输入您的性别:')
user_age = input('请输入您的年龄:')
user_school = input('请输入您的学校:')

# 4.星号的优化:
#多个星号这样输出：
print('*'*30)  # 数字30就是你要几个星号；

# 5.部分多余代码：
# 这个是做什么的呢？可以删除（可以在输出直接嵌入，看六）
name1='姓名:'
xingbie1='性别:'
age1='年龄:'
school1='学校:'
kongge=input()

# 6.输出修改：
print('正在生成您的简历......')
print('******************************')
print('             简历      ')
print('姓名：'+user_name)
print('性别:'+user_sex)
print('年龄:'+user_age)
print('学校:'+user_school)
print('over thanks')
    
# 好整体就是这样，希望下次看见你的代码有所提升哦，一起加油吧！