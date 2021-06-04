age = input("input age:>>>")
age_lst = list(range(18, 30))
yunshi = {
	"18": "大好青春，不过现阶段工资低又找不到对象，不过前途仍然不可限量，趁没对象抓紧赚钱吧！",
	"19": "别预测了，学习吧"
	}
while True:
	# if age in age_lst and age.isdigit():
	if age.isdigit():
		if int(age) in age_lst:
			print(yunshi.get(age, "无结果！"))
			break
		else:
			print("inout erro!")
			age = input("input age:>>>")
	else:
		print("inout erro!")
		age = input("input age:>>>")