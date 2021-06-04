print("Hello,your personal information are going to be collected to make a resume.You will be asked eight questions!\n")
name = input('1/8    Please tell me your name>>>>')
print("This is a good name!\n")
sex = input('2/8    Ok!' + name +',please tell me your sex>>>>')
age = input('\n3/8    How old are you>>>>')
school = input('\n4/8    Where are you graduated>>>>')
telephone = input("\n5/8    What's your telephone number>>>>")
email = input("\n6/8    What's your email address>>>>")
Marriage = input('\n7/8    Have you got Married>>>>')
print('\n8/8    Thank you,' + name + 
	'!Now please tell me something about yourself!')
print('What you say will serve as your profile!')
profile = input('>>>>')
print('\nThank you for your cooperation!Please hand on a second!')
print('\nyour information are being cleared up!\n')
print('*'*20)
print('\n')
print('       RESUME\n')
print('\nName:     '+name)
print('Sex:      '+sex)
print('Age:      '+age)
print('School:   '+school)
print('Married:  '+Marriage)
print('Telephone:'+telephone)
print('Email:    '+email)
print('Profile:  '+profile)

# 整体来说，思路清晰从输入到输出整体给出的代码清晰。
#但，对于之后的多人协作完成某个项目，就需要更加清晰快速定位，所以我们需要做出如下几点优化：
# 1.划分区域；
# 2.变量名再更加直观一些；
# 3.为了使代码更具有观赏性，建议：在赋值号两边加上空格；(你已经做到了不错）
# 4.星号的优化；（你已经做到了）
# 6.在print当中，能不掉用函数尽量不调用，为了提升代码运行效率；
# 7.简历内容可以更加完善；（不做示例）
# 8.是否可以加个输入判断？
# 9.知识点：Python中print()函数自带换行；水平制表符\t
# 扩展可以添加一个动态效果，在这里我就不讲述，自己有兴趣去查找一下；（初步达到动态效果import time）
# 注意：文件命名不要用“-”要用这个："_":就是这样命名：my_report.py
# 也不要用数字开头命名！！！！
#修改demo：
# 1.划分区域与input后的括号应使用英文输入法下的括号，不要使用中文输入法下括号！！！(此条为提醒）
#<----------------user_input_area--------------->
print("Hello,your personal information are going to be collected to make a resume.You will be asked eight questions!\n")
name = input('1/8    Please tell me your name>>>>')
print("This is a good name!\n")
sex = input('2/8    Ok!' + name +',please tell me your sex>>>>')
age = input('\n3/8    How old are you>>>>')
school = input('\n4/8    Where are you graduated>>>>')
telephone = input("\n5/8    What's your telephone number>>>>")
email = input("\n6/8    What's your email address>>>>")
Marriage = input('\n7/8    Have you got Married>>>>')
print('\n8/8    Thank you,' + name + 
	'!Now please tell me something about yourself!')
print('What you say will serve as your profile!')
profile = input('>>>>')
#<----------------print_area--------------->
print('\nThank you for your cooperation!Please hand on a second!')
print('\nyour information are being cleared up!\n')
print('*'*20)
print('\n')
print('       RESUME\n')
print('\nName:     '+name)
print('Sex:      '+sex)
print('Age:      '+age)
print('School:   '+school)
print('Married:  '+Marriage)
print('Telephone:'+telephone)
print('Email:    '+email)
print('Profile:  '+profile)

# 2.变量名再更加直观一些:(此条为其他同学问题，作为提醒你，加深印象！)
# 因为有时候输入的内容很多，你得区分哪些是系统输入变量，哪些是人工输入变量。
# 英文版：(Because sometimes there is a lot of input, you have to distinguish between system input variables and manual input variables.)
# 在变量前面加个user即可(并尽量用英文）；
# 部分代码示例：

user_name = input('1/8    Please tell me your name>>>>')
user_sex = input('2/8    Ok!' + name +',please tell me your sex>>>>')
user_age = input('\n3/8    How old are you>>>>')
user_school = input('\n4/8    Where are you graduated>>>>')


# 4.星号的优化:
#多个星号这样输出：(你已经做到）
print('*'*30)  # 数字30就是你要几个星号；
# 5.在print当中，能不掉用函数尽量不调用，为了提升代码运行效率；（作为提醒）

# 7.简历内容可以更加完善；（不做示例）

# 8.是否可以加个输入判断？
# 示例：
#输入性别并判断
while True:
    gender = input('请输入您的性别（男/女）：>')
    if gender == '男' or gender == '女':
        break
    else:
        print('性别输入错误')

#输入年龄并判断
while True:
    age = input('请输入您的年龄：>')
    if age.isdigit():
        break
    else:
        print('年龄输入错误')
# 9.水平制表符\t
# 你代码中字符串很多空格，不美观也显得不够专业，用水平制表符更加完美！
# 部分代码示例：

print('\t\tRESUME\n')
print('\nName:\t\t\t'+name)

        
# 好整体就是这样，希望下次看见你的代码有所提升哦，一起加油吧！