print('-'*3, '与电脑猜拳', '-'*3)
# <--------import_area--------->
import random

# <--------Data_area----------->
dict_c = {1:'石头', 2:'剪刀', 3:'布'}
dict_u =  {'石头':1, '剪刀':2, '布':3, 'Python':1}

# <--------user_input_area----->
user = input('请输入：(只能是石头/剪刀/布)')
user1 = dict_u.get(user, 'null')
computer = random.randint(1,3)
c = dict_c[computer]

# <--------if_area------------->
if user != '石头' and user != '剪刀' and user != '布':
    print('你又调皮了，只能输入石头/剪刀/布')
else:
print('电脑出：', c)
    print("输赢结果：")
    if user == c:
        print('平手')
elif user1 == 1 and computer == 3:
    print('你输啦')
    elif user1 == 2 and computer == 1:
        print('你输啦')
elif user1 == 3 and computer == 2:
        print('你输啦')
    else:
    print('你走狗屎运了')