user_answer_correct = False

#提问用户性别
while not user_answer_correct:
    user_gender = input("请输入你的性别（F/M):")
    if user_gender != "F" and user_gender != "M":
        print("输入不正确，请输入F/M")
    else:
        user_answer_correct = True


"""提问用户是否单身
    如果用户单身，就祝他能找到对象
    如果不单身，就祝他和对象百年好合"""
user_answer_correct = False
while not user_answer_correct:
    single_or_not = input("你是否单身？（T/F):")
    if single_or_not == "T" and user_gender == "F":
        yunshi1 = "祝你能找到男朋友"
        user_answer_correct = True
    elif single_or_not == "T" and user_gender == "M":
        yunshi1 = "祝你能找到女朋友"
        user_answer_correct = True
    elif single_or_not == "F":
        yunshi1 = "祝你和对象百年好合"
        user_answer_correct = True
    elif single_or_not != "T" and single_or_not != "F":
        print("输入不正确，请输入T/F")
    else:
        print ("none")

"""提问用户年龄
    如果18岁以内，就祝他能上985本科
    如果18-23，就祝他能上985研究生
    如果23以上，就祝他事业有成"""
user_answer_correct = False
while not user_answer_correct:
    user_age = input("请输入你的年龄:")
    if user_age <= "18" and user_age >= "1":
        yunshi2 = "祝你能考上985本科"
        user_answer_correct = True
    elif user_age > "18" and user_age < "23":
        yunshi2 = "祝你能考上985研究生"
        user_answer_correct = True
    elif user_age >= "23":
        yunshi2 = "祝你事业有成"
        user_answer_correct = True
    else:
        print("输入不正确，请输入0-100的数字")

user_answer_correct = False

print("*******正在生成你的运势*******")
print(yunshi1)
print(yunshi2)
