print("hello,I'd like to predict your fortune.Please anwser some questions.")
special_predict = ""
#<-----------------------------user_input_area------------------------------->
#<------------1/3_input_sex------------->
while True:
	user_sex = input("\n1/3\tAre you a female or a male?(F/M)>>>>")
	if user_sex == "F" :
		print("	You are a woman!")
		special_predict += "You will meet a spectacular boy friend in six years!And "
		break
	elif user_sex == "M" :
		print("	You are a man!")
		special_predict += "You will find a lovely girl friend in five years!And "
		break
	else:
		print("This isn't a propreating anwser!Please press 'F' or 'M'!")	
#<------------2/3_input_age------------->
while True:
	user_age = input("\n2/3\tHow old are you?>>>>")
	if user_age.isdigit():
		if int(user_age) <= 17:
			special_predict += "You will be admitted to Qinghua University!"
		else:
			special_predict += "You will get a job with 10 thousand yuan a month!"
		break
	else:
		print("This isn't a propreating anwser!Please press your age!")
#<------------3/3_input_num------------->
while True:
	user_num = input("\n3/3\tWhat is your last number of your phone number?>>>>")
	if user_num.isdigit():
		if int(user_num) == 1 or 3 or 5 or 9:
			special_predict += "You will make a awesome speech in social media!"
		elif int(user_num) == 2 or 7 or 0:
			special_predict += "You will put out some good works and get VIP attention!"
		else:
			special_predict += "BUT!!!It's easy to make a big argument about your relationship!"
		break
	else:
		print("This isn't a propreating anwser!Please press a number which is your last number of your phone number!")
#<-------------------------------print_area--------------------------------->
print('\nThank you for your cooperation!Please hand on a second!')
import time
time.sleep(2)
print("\nOK!Thank you for your cooperation!Your fortune is here!\n")
time.sleep(1)
print("*"*25 + "your fortune of This year" + "*"*25)
print(special_predict)


# 整体来说，思路清晰从输入到输出整体给出的代码清晰。
# 如下几点需要注意的：
# 1.有没有想过用代码函数代替这些while循环呢？（此为扩展，不做示例）
# 2.在代码运行当中，我个人更加喜欢在不必要的使用while循环时不使用，或者尽量用if之类的判断语句来判断。
# 3.为代码划分区域；（你做到了，继续保持）

# 2.在代码运行当中，我个人更加喜欢在不必要的使用while循环时不使用，或者尽量用if之类的判断语句来判断。
# 就例如这个（看不懂没事，之后在算法课第一节也会讲到）小咖学员有体验课：
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

# 加油哦！AI悦创