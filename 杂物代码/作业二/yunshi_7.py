print('峰回路转，你跋山涉水来到此处。仙气弥漫，隐约见一老者打坐石畔，仙风鹤骨，静闭双眼，你打算问问他前路状况。')

user_answer_correct = False

import time
time.sleep(2)


gender = input('"来者何人？侠客还是仙女？"')

while not user_answer_correct:
	if gender =='侠客':
		import time
		time.sleep(1)
		age = input('"敢问兄台年岁？"')
		user_answer_correct = True
	elif gender =='仙女':
		import time
		time.sleep(1)
		age = input('"敢问姑娘芳龄？"')
		user_answer_correct = True
	else:
		import time
		time.sleep(1)
		gender = input('"听不清！说清楚些！侠客还是仙女？"')

import time
time.sleep(1)

print( )
print('*'*10+'前路运势'+'*'*10)
print( )

import time
time.sleep(1)


if gender =='侠客' and int(age)>=18:
	print('侠客风流潇洒、器宇不凡，在这个不用亮剑的时代里，倘若剑气不泯，定能剑啸长虹。')
elif gender =='侠客' and int(age)<18:
	print('少年骨骼精奇、聪明神慧，不懈追逐梦想，天地间最伟大的诗篇中必定有你。')
elif gender =='仙女' and int(age)>=18:
	print('仙女长怀善意、心怀诗意，必将在最美的年华迎接自己生命中的一轮明月。')
elif gender =='仙女' and int(age)<18:
	print('小仙女俊俏可爱、清新自然，前路鲜花为你绽放。')
    
    

# 整体来说，思路清晰从输入到输出整体给出的代码清晰。
# 如下几点需要注意的：
# 1.可以试一试用函数封装一下代码；（此为扩展，不做示例）
# 2.在代码运行当中，我个人更加喜欢在不必要的使用while循环时不使用，或者尽量用if之类的判断语句来判断。减少代码的冗余。
# 3.为代码划分区域；(不做示例）
# 4.实现了一些动态效果，那我们有没有想过，把用户输入的清空，就显示输出结果呢？在time的基础上扩展：
# 举个栗子：（自己单独敲一下，然后在cmd运行试一试哈！）
#<-------------------------导入库----------------------->
import time
import os
#<------------------------print_area-------------------->
print('''
		huxhhhwdcbdhsdcssgdcdsc
		dcdcssshcuhsdshudushuhhshvsvshvsv

		vsvsvishvsvhshvissv
		''')
time.sleep(1)
os.system('cls')
print('''
	huhhuhhhhhuhhhhu
	jijijijjjjjijijjjjji
	huhuhuhuhuhhuhhuh
	hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
	''')



# 2.在代码运行当中，我个人更加喜欢在不必要的使用while循环时不使用，或者尽量用if之类的判断语句来判断。
# 就例如这个（看不懂没事，之后在算法课第一节也会讲到）小咖学员有体验课：有兴趣私我（有优惠）
# 统计一篇文章的词频部分代码：
def find_word_count(words):
#意见优化的，减少for循环是使用；
    # word_count_dict = {}   #局部范围字典
    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1  #word 本身就算一个单词
#未优化的，两个for循环，这篇文章如果有一千字的话，就得循环两千次左右。而上面一个for循环，循环单词本身的数量就行，运行速度有明显的差异。
    # for word in set(words):
    #   word_count_dict[word] = 0
    # for word in words:
    #   word_count_dict[word] += 1
    return word_count_dict

# 具体如何实现，可以参考简历修改的代码封装示例的思路来。

# 3.为代码划分区域；
# 就例如简历生成中的形式：


# ......
# 加油哦！AI悦创
    