import random

# 输入性别或退出
while True:
	gender = input('请输入您的性别（F/M），输入（exit）退出：\r\n')
	if gender.upper() == 'F' or gender.upper() == 'M':
		gender = gender.upper()
		break
	elif gender.upper() == 'EXIT':
		print('\r\n\r\n感谢使用，再见！')
		exit()
	else:
		print('您的输入有误，请重新输入\r\n')

# 输入年龄并判断年龄层
while True:
	age = input('请输入您的年龄（0-100）：\r\n')
	try:
		age = int(age)
		if 0 <= age <= 100:
			break
		else:
			print('您的输入有误，请输入0-100的整数\r\n')
	except:
		print('您的输入有误，请输入0-100的整数\r\n')


# 定义函数
def fortune_test(gender, age):
	you = 0
	if 0 <= age < 18:
		you = 1
	elif age == 18:
		you = 2
	elif 18 < age < 30:
		you = 3
	elif 30 <= age < 60:
		you = 4
	
	# 判断年龄层并打印随机字符串
	if you == 3:
		if gender == 'F':
			lucky = ['找到女朋友', '继承巨额财富', '找到好工作', '买彩票中500万大奖', '创业成功，收获天使轮投资']
			unlucky = ['被好兄弟绿', '北漂失败，落魄回家', '丢掉工作，女友坐上别人的宝马车', '创业失败，欠下巨额债务']
			case_list = random.choice([lucky, unlucky])
			case_len = len(case_list)
			random_index = random.randint(0, case_len - 1)
		else:
			lucky = ['找到男朋友', '继承巨额财富', '找到好工作', '买彩票中500万大奖', '创业成功，收获天使轮投资']
			unlucky = ['被闺蜜绿', '北漂失败，落魄回家', '丢掉工作，男友的宝马车副驾坐着别的妹子', '创业失败，欠下巨额债务']
			case_list = random.choice([lucky, unlucky])
			case_len = len(case_list)
			random_index = random.randint(0, case_len - 1)
		print('在接下来的{time}个月,你会{case}。'.format(case=case_list[random_index], time=random.randint(1, 12)))
	
	elif you == 1:
		lucky = ['顺利升学', '发现亲爹很有钱', '拿到三好学生', '期末全过', '考神附体']
		unlucky = ['挂科留级', '作弊被发现', '因打架被全校通报批评，记大过处分一次', '因父母参加家长会发现你成绩垫底而被揍']
		case_list = random.choice([lucky, unlucky])
		case_len = len(case_list)
		random_index = random.randint(0, case_len - 1)
		print('在接下来的{time}个月,你会{case}。'.format(case=case_list[random_index], time=random.randint(1, 12)))
	
	elif you == 2:
		school_list = ['复旦大学', '剑桥大学', '哈佛大学', '麻省理工大学', '斯坦福大学', '蓝翔职业技术学院', '克莱登大学', '中关村应用文理学院', '五道口职业技术学院',
		               '陈经纶中学附属大学', '定福庄大学']
		school = school_list[random.randint(0, len(school_list) - 1)]
		if gender == 'F':
			lucky = ['找到女朋友', '继承巨额财富', '拿到全额奖学金', '买彩票中500万大奖', '获得本校报送硕博连读机会']
			unlucky = ['被发好人卡', '被告知成绩单寄错地址，你并没有被学校录取', '被调剂至水暖系烧锅炉专业', '发现班上并没有一个女生']
			case_list = random.choice([lucky, unlucky])
			case_len = len(case_list)
			random_index = random.randint(0, case_len - 1)
		else:
			lucky = ['找到男朋友', '继承巨额财富', '拿到全额奖学金', '买彩票中500万大奖', '获得本校报送硕博连读机会']
			unlucky = ['被闺蜜绿', '被告知成绩单寄错地址，你并没有被学校录取', '被调剂至家政系擦玻璃专业', '发现班上全是女生，你的校园恋爱梦彻底破灭']
			case_list = random.choice([lucky, unlucky])
			case_len = len(case_list)
			random_index = random.randint(0, case_len - 1)
		print('你会考上{school}，并{case}。'.format(case=case_list[random_index], school=school))
	
	elif you == 4:
		
		if gender == 'F':
			lucky = ['喜得一子', '升职加薪', '公司上市，作为管理层而获得公司干股，陡然而富', '买彩票中500万大奖', '家族企业获得红杉资本领投，B轮融资达到1.2亿']
			unlucky = ['发现妻子出轨', '北漂失败，落魄回家', '丢掉工作，妻子与你离婚并嫁给一位暴发户', '生意失败，欠下巨额债务，在自杀边缘几经挣扎，就此沉沦']
			case_list = random.choice([lucky, unlucky])
			case_len = len(case_list)
			random_index = random.randint(0, case_len - 1)
		else:
			lucky = ['为丈夫生下一子', '升职加薪', '公司上市，作为管理层而获得公司干股，陡然而富', '买彩票中500万大奖', '家族企业获得红杉资本领投，B轮融资达到1.2亿']
			unlucky = ['发现丈夫出轨', '北漂失败，落魄回家', '丢掉工作，丈夫与你离婚并与一20岁嫩模结婚，你净身出户', '生意失败，欠下巨额债务，在自杀边缘几经挣扎，就此沉沦']
			case_list = random.choice([lucky, unlucky])
			case_len = len(case_list)
			random_index = random.randint(0, case_len - 1)
		
		print('在接下来的{time}个月,你会{case}。'.format(case=case_list[random_index], time=random.randint(1, 12)))
	
	else:
		if gender == 'F':
			title = '老爷子'
		else:
			title = '老太太'
		
		print('{title}，您已经{age}高龄，此生命数已定，您已知天命。在以后的日子里，您子孙满堂，坐享天伦之乐。'.format(title=title, age=age))


# 执行函数
print('\r\n\r\n====您的运势====\r\n\r\n')
fortune_test(gender, age)

# 退出程序
print('\r\n\r\n感谢使用，再见！')
exit()


# 整体来说，思路清晰从输入到输出整体给出的代码清晰。
# 如下几点需要注意的：
# 1.已经初步实现代码封装之美，在fortune_test()函数块中已经体现；
# 2.在代码运行当中，我个人更加喜欢在不必要的使用while循环时不使用，或者尽量用if之类的判断语句来判断。
# 3.为代码划分区域；

# 2.在代码运行当中，我个人更加喜欢在不必要的使用while循环时不使用，或者尽量用if之类的判断语句来判断。
# 就例如这个（看不懂没事，之后在算法课第一节也会讲到）小咖学员有体验课：
# 统计一篇文章的词频部分代码：
# def find_word_count(words):
# 	# 意见优化的，减少for循环是使用；
# 	# word_count_dict = {}   #局部范围字典
# 	for word in words:
# 		if word in word_count_dict:
# 			word_count_dict[word] += 1
# 		else:
# 			word_count_dict[word] = 1  # word 本身就算一个单词
# 	# 未优化的，两个for循环，这篇文章如果有一千字的话，就得循环两千次左右。而上面一个for循环，循环单词本身的数量就行，运行速度有明显的差异。
# 	# for word in set(words):
# 	#   word_count_dict[word] = 0
# 	# for word in words:
# 	#   word_count_dict[word] += 1
# 	return word_count_dict


# 具体如何实现，可以参考简历修改的代码封装示例的思路来。

# 3.为代码划分区域；
# 就例如简历生成中的形式：
# 1.划分区域：
# 虽然，你已经有写这样在每行代码上注释，但可以划分区域，使代码更加清晰明了。
# <----------------user_input_area--------------->
# 输入姓名
name = input('请输入您的姓名：>')
# 输入毕业院校
# ......
# <----------------while_area--------------->
# 输入性别并判断
# while True:
# # ......
# # 输入年龄并判断
# while True:
# ......
# <----------------print_area--------------->
# 格式
print('正在生成简历......')
print('\r\n')
# ......
# 加油哦！AI悦创
