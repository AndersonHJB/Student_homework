"""
1. 代码多，代码多不是问题「简洁」
2. 获取较为完整的用户信息，并保存下来
3. Plus：每个用户使用单独保存一个 txt 文件，并且保存运势数据
4. list>>>dict
5. Plus：把全部代码改写成函数「能改写就改写」
"""
# --------user inpit---------
username = input("请输入你的名字：")
gender = input("请输入您的性别（男/女)：")

# ages = int(input("请输入您的年龄(18~75):"))
ages = input("请输入您的年龄(18~75):")
# ages = int(age)
time = input("请输入您的生辰是(白天/晚上):")

with open("data/yunshi.txt", "a+", encoding="utf-8")as fp:
    fp.write(str(
        {
        "username": username, 
        "gender": gender,
        "age": ages,
        "time": time
        }
        ) + "\n\n")


# --------range area---------
a = list(range(18, 26))
b = range(26, 36)
c = range(36, 46)
d = range(46, 56)
e = range(56, 66)
f = range(66, 76)

# --------data area---------
user_gender = ('男', '女')
user_time = ('白天', '晚上')

M1_day = (a, '男', '白天')
M2_day = (b, '男', '白天')
M3_day = (c, '男', '白天')
M4_day = (d, '男', '白天')
M5_day = (e, '男', '白天')
M6_day = (f, '男', '白天')

M1_night = (a, '男', '晚上')
M2_night = (b, '男', '晚上')
M3_night = (c, '男', '晚上')
M4_night = (d, '男', '晚上')
M5_night = (e, '男', '晚上')
M6_night = (f, '男', '晚上')

F1_day = (a, '女', '白天')
F2_day = (b, '女', '白天')
F3_day = (c, '女', '白天')
F4_day = (d, '女', '白天')
F5_day = (e, '女', '白天')
F6_day = (f, '女', '白天')

F1_night = (a, '女', '晚上')
F2_night = (b, '女', '晚上')
F3_night = (c, '女', '晚上')
F4_night = (d, '女', '晚上')
F5_night = (e, '女', '晚上')
F6_night = (f, '女', '晚上')

M1 = "大好青春，不过现阶段工资低又找不到对象，不过前途仍然不可限量，趁没对象抓紧赚钱吧！"
M2 = "三十而立是骗人的，正当年，狠狠的奋斗吧"
M3 = "对孩子有点耐心"
M4 = "不要以为自己什么都知道"
M5 = "养生了么"
M6 = "洗洗早点睡"

M1s = "别预测了，学习吧"
M2s = "边学，边赚钱"
M3s = "还得继续干"
M4s = "活到老干到老"
M5s = "不要找小三"
M6s = "想找也不行了吧"

F1 = "女娃娃要爱惜自己"
F2 = "不要整容还小"
F3 = "对老公好一点"
F4 = "活到老学到老"
F5 = "真想整容就搞吧"
F6 = "别老跳舞"

F1s = "不要乱花钱"
F2s = "经济要独立"
F3s = "对孩子好一点"
F4s = "你去整容吧"
F5s = "打扮精神点"
F6s = "洗洗睡吧"

ku = {M1_day: M1,
      M2_day: M2,
      M3_day: M3,
      M4_day: M4,
      M5_day: M5,
      M6_day: M6,
      M1_night: M1s,
      M2_night: M2s,
      M3_night: M3s,
      M4_night: M4s,
      M5_night: M5s,
      M6_night: M6s,
      F1_day: F1,
      F2_day: F2,
      F3_day: F3,
      F4_day: F4,
      F5_day: F5,
      F6_day: F6,
      F1_night: F1s,
      F2_night: F2s,
      F3_night: F3s,
      F4_night: F4s,
      F5_night: F5s,
      F6_night: F6s
      }

age_g = (a, b, c, d, e, f)

if ages in range(18, 76):
    for rg in age_g:
        if ages in rg:
            pass
            break

if gender in user_gender:
    pass
if time in user_time:
    pass

user_key = (rg, gender, time)

for new in ku:
    if user_key == new:
        yu_ce = ku.get(new)
        print(f"尊敬的用户您好！为您预测的运势结果如下：'{yu_ce}'")
        break



print("\t***你今年的运势***")


