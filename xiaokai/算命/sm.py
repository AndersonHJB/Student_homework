a = range(18, 20)
aa = list(a)

M1_day = (18, '男')
M2_day = (19, '男')

M1_night = (18, '男')
M2_night = (19, '男')

F1_day = (18, '女')
F2_day = (19, '女')

F1_night = (18, '女')
F2_night = (19, '女')

M1 = "大好青春，不过现阶段工资低又找不到对象，不过前途仍然不可限量，趁没对象抓紧赚钱吧！"
M2 = "不要以为自己什么都知道"

M1s = "别预测了，学习吧"
M2s = "边学，边赚钱"

F1 = "女娃娃要爱惜自己"
F2 = "不要整容还小"

F1s = "不要乱花钱"
F2s = "经济要独立"

ku = {M1_day: M1,
      M2_day: M2,
      M1_night: M1s,
      M2_night: M2s,
      F1_day: F1,
      F2_day: F2,
      F1_night: F1s,
      F2_night: F2s
      }

# --------输入性别---------
user = input("请输入您的名字：")
gender = input("请输入您的性别（男/女)：")


# --------判断性别的输入是否正确---------
def user_gender(gd):
    while True:
        if gd == '男':
            return gd
        elif gd == '女':
            return gd
        else:
            gd = input("请选择男/女")

dd = user_gender(gender)

# --------输入年龄---------
age = input("请输入您的年龄(18~19):")


# --------判断年龄输入是否正确---------
def user_ms(ms):
    while True:
        if ms.isdigit():
            if int(ms) in a:
                return int(ms)
            else:
                ms = input("请在指定范围内")
        else:
            ms = input("年龄需要数字>>")

cc = user_ms(age)


# --------合并两个函数成一个元组---------
user_key = (cc, dd)

# --------判断元组是否与字典key一致，并打印值---------
print("\t***你今年的运势***")

for new in ku:
    if user_key == new:
        yu_ce = ku.get(new)
        print(f"尊敬的用户您好！为您预测的运势结果如下：'{yu_ce}'")
        break

# --------存储用户信息及算命结果---------

with open("data/user.txt", "a+", encoding="utf-8")as xk:
    xk.write(str(
        {
        "用户名": user,
        "性别": gender,
        "年龄": age,
        "结果": yu_ce
        }
        ) + "\n\n")