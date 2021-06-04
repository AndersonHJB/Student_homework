#***********输入区**********
dorm=input('请输入你的宿舍：')
name=input('请输入你的名字：')
age=int(input('请输入你的年龄：'))

#**********输出区***************
a=['355','357']
b=['吴凡','王叶威','孙宇航','李江波','王浩']
c=['李承志','郭霖','蒋天晖','王浩冲','李文通','付鹤泉']
if dorm in range(a):
	if dorm=='355':
		if name in range(b):
			if age>18:
				print(f'{name}见多识广，思想成熟；')
			else :
				print(f'{name}活力四射，精力充沛；')	
			if name=='吴凡':
				print(f'你是{dorm}宿舍长{name}，品行端正，关心他人，学习认真，宿舍长当之无愧。')
			elif name=='王叶威':
				print(f'你是{dorm}领奖学金的男人{name}，内心善良，懂礼貌，性格率真。')
			elif name=='孙宇航'	:
				print(f'你是{dorm}群主{name}，慷慨率真，心地善良，又可爱又调皮，张嘉伟表示想掐脸脸。')
			elif name=='李江波':
				print(f'你是{dorm}年龄最小的{name}，性格温和，年龄最小，宿舍的大家会保护你的，你要向吴凡学习呀！')
			else:
				print('浩哥是团支书,日理万机,要注意休息呀.')
		else:
			print('憨批！你自己的名字都打错')				
	else:
		if name in range(b):
			if age>18:
				print(f'{name}见多识广，思想成熟；')
			else :
				print(f'{name}活力四射，精力充沛；')
			if name=='付鹤泉':
				print(f'你是{dorm}的{name}，泉泉可爱。')
			elif name=='李文通':
				print(f'你是{dorm}的{name}，物理竞赛大佬。')
			elif name=='李承志'	:
				print(f'你是{dorm}的{name}，又可爱又调皮，张嘉伟表示想掐脸脸。')
			elif name=='郭霖':
				print(f'你是{dorm}的{name}，郭霖小可爱，撩妹呢？')
			elif name=='蒋天晖':
				print(f'你是{dorm}的{name}，晖哥NB')
			else:
				print(f'你是{dorm}的王浩冲，聪敏又见多识广。')	
		else:
			print('憨批！你自己的名字都打错，奖励亲你一口！')	

else :
	print('憨批！你自己的宿舍都不知道，！')

