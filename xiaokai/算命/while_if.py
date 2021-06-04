age = input("input age:>>>")
age_lst = list(range(18, 30))
while True:
	# if age in age_lst and age.isdigit():
	if age.isdigit():
		if int(age) in age_lst:
			print("age:>>>", age)
			break
		else:
			print("inout erro!")
			age = input("input age:>>>")
	else:
		print("inout erro!")
		age = input("input age:>>>")