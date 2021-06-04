#<---------初始设置----------->    # 点赞，做到了前面的修改意见，不错哦！但要是把初始化设置改成导入模块或库九更好咯！
import time
import random


time.sleep(1)         # 有想到使用动态效果，不错哦！

class Role():
	def __init__(self,hp,name):
		self.hp = hp
		self.name = name
	

	def live(self):
		if self.hp <= 0:
			return False
		else :
			return True

	def being_attack(self,attack_value):
		self.hp = self.hp - attack_value

	def show_status(self):
		print('{}\'：剩余血量： {}.'.format(self.name,self.hp))

hero_attack = 10
monster_attack=random.randint(15,20)





#<------------显示------------>
user_input_name = input('请告诉我你的名字>')   # 做到给用户命名的机会，不错，其他小伙伴有些直接把玩家名命名了。

print('你好!\000'+user_input_name)

time.sleep(0.1)

print('欢迎来到决斗场')
time.sleep(1)

print('你是这个城镇上的英雄，前不久来了一个大怪兽，袭击城镇。')
time.sleep(0.3)

print('你与怪兽大战了三百回合，还未决出胜负，但城镇已经不住战斗了，于是，你孤注一掷，将怪兽引到了带有封印的决斗场')
time.sleep(0.3)

print('现在，不是你死，就是它亡')
time.sleep(0.3)

confidence=input('你准备好了吗?(Y/N)')
if confidence == 'Y':
	print('我们开始')

elif confidence == 'N':
	print('那也得上咯')

print('规则:你可以选择攻击、闪躲或是反弹')
time.sleep(2)
print('攻击有三种方式：1投毒：给对手造成10点伤害并使对手的下次攻击伤害减半。')
time.sleep(2)
print('2.重击：有可能造成20点伤害，但由于速度太慢可能会被对手躲掉')
time.sleep(2)
print('3.普攻：给对手造成15点伤害')
time.sleep(2)
print('闪躲：可以使你躲掉这次攻击，相应的，无法对对手造成伤害')
time.sleep(2)
print('反弹：你受到对手40%---60%的伤害，同时反弹回剩余伤害')
time.sleep(2)
print('初始设定：你有100点血，怪兽有120点血，且怪兽每次都会攻击（兽性），基础伤害为15-20')

time.sleep(5)
print('游戏开始')           # 这一段的停顿，看似乎每次sleep两秒，但连起来九有点占用时间了，用户体验会不好许多，个人觉得一秒九差不多了。

hero = Role(100,user_input_name)
monster = Role(120,'monster')	


while hero.live() and monster.live():
	print('系统提示')
	hero.show_status()
	monster.show_status()

	fangshi1_user_input = input('请选择攻击、闪躲或反弹(A/D/R)>')

	if fangshi1_user_input == 'A':
		fangshi2_user_input=input('请选择攻击方式（1/2/3):')
		if fangshi2_user_input == '1':
			hero_attack_value = hero_attack
			monster_attack_value = monster_attack*0.5
			monster.being_attack(hero_attack_value)
			hero.being_attack(monster_attack_value)
			print('你已经投毒成功，对对手造成了10点伤害并使其下次攻击伤害减半！')
			time.sleep(1)
			print('等待对手攻击......')
			time.sleep(3)
			print('对手攻击了你，并对你造成' + str(monster_attack_value) + '点伤害')
		elif fangshi2_user_input == '2':
			hero_attack_value = hero_attack*random.choice([0,2]) 
			monster_attack_value = monster_attack
			monster.being_attack(hero_attack_value)
			hero.being_attack(monster_attack_value)
			if hero_attack_value == 0:
				print('十分遗憾，你的攻击被对手躲过了')
			else :
				print('恭喜，你成功对对手施加暴击并造成了20点伤害')
			time.sleep(1)
			print('等待对手攻击......')
			time.sleep(3)
			print('对手攻击了你，并对你造成' + str(monster_attack_value) + '点伤害')
		elif fangshi2_user_input == '3':
			hero_attack_value = hero_attack + 5
			monster_attack_value = monster_attack
			monster.being_attack(hero_attack_value)
			hero.being_attack(monster_attack_value)
			print('你对对手进行了普攻，减掉其15点血')
			time.sleep(1)
			print('等待对手攻击......')
			time.sleep(3)
			print('对手攻击了你，并对你造成' + str(monster_attack_value) + '点伤害')

	elif fangshi1_user_input == 'D':
		pass
		print('你进行了闪避，躲过了攻击')

	elif fangshi1_user_input == 'R':
		monster_attack_value = monster_attack*random.choice([0.4,0.5,0.6])
		hero_attack_value = monster_attack - monster_attack_value 
		monster.being_attack(hero_attack_value)
		hero.being_attack(monster_attack_value)
		print('你用了反弹技能')
		time.sleep(1)
		print('等待对手攻击')
		time.sleep(3)
		print('对手攻击了你，对你造成'+ str(monster_attack_value) + '点伤害，同时你反弹给对手' + str(hero_attack_value) +'点伤害')

		time.sleep(3)
		
hero.show_status()
monster.show_status()

print('游戏结束')


if hero.live():
	print('恭喜你，打败了怪兽，守护了城镇')

elif monster.live():
	print('很遗憾，你失败了，未能成功守护城镇')

else:
	print('你牺牲了，但你成功守护住了这个美丽的城镇，向你致敬！')
    
    
# 整体的代码逻辑都不错哦，还有就是一部分修改意见在上面，认真看看哦。
# 试一试把这一段写出函数：
print('规则:你可以选择攻击、闪躲或是反弹')
time.sleep(2)
print('攻击有三种方式：1投毒：给对手造成10点伤害并使对手的下次攻击伤害减半。')
time.sleep(2)
print('2.重击：有可能造成20点伤害，但由于速度太慢可能会被对手躲掉')
time.sleep(2)
print('3.普攻：给对手造成15点伤害')
time.sleep(2)
print('闪躲：可以使你躲掉这次攻击，相应的，无法对对手造成伤害')
time.sleep(2)
print('反弹：你受到对手40%---60%的伤害，同时反弹回剩余伤害')
time.sleep(2)
print('初始设定：你有100点血，怪兽有120点血，且怪兽每次都会攻击（兽性），基础伤害为15-20')
# 把游戏内部代码做成函数隐藏，就留下用户交互就行（扩展）


# 好，这次问题比较少，给自己加个鸡腿哦。继续加油！！！
# AI悦创




