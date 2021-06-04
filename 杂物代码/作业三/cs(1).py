#<-----------------导入数据库区域------------------->
import random

#<---------------------玩家输入区------------------------->

user_player_name1 = input('请设定玩家名称：')
user_enemy_name2 = input('请设定敌人名称：')
user_enemy_name3 = input('请设定敌人名称：')


#<------------------类函数区域------------------------>
class Greature():
	def __init__(self,hp,name):    #③hp：生命值
		self.hp = hp          #⑤有生命值之后呢？我就可以开始定义：判断是否已经死了。
		self.name = name 

	def attack(self):
		attack_value = random.randint(0,50)
		return attack_value

	def attack2(self):
		attack2_value = random.randint(0,50)
		return attack2_value

	def being_attack(self,attack_value):
		self.hp = self.hp - attack_value

	def being_attack2(self,attack2_value):
		self.hp = self.hp - attack2_value
		
	def not_dead(self):    #not_dead:（是）不是没有死。
		if self.hp <= 0:    #因为已经小于零了，所以:
			return False   #False:{问：是不是没有死。答：不，死了。所以输出错的——False}
		else:
			return True

	def show_status(self):
		print('{}\'s hp is{}.'.format(self.name,self.hp))      #展示玩家与敌人的hp值 





#<--------------------输出与调用区域------------------->

player = Greature(100,user_player_name1)   #②如果需要填入初始值的话，那我们就是需要在class（类）里面提前定义这个值。/预设的地方。
enemy = Greature(80,user_enemy_name2)   #②如果需要填入初始值的话，那我们就是需要在class（类）里面提前定义这个值。/预设的地方
enemy2 = Greature(80,user_enemy_name3)

#<--------------------while循环区---------------------->
#游戏嘛，我们要判断当前的游戏状态。player is die or enemy die
while player.not_dead() and enemy.not_dead(): #①如何判断呢？那我们就需要你个初始换的声明值（血条）

	player.show_status()
	enemy.show_status()
	enemy2.show_status()


	user_input = input('Attack or Defence(A/B/D):')
	if user_input != 'A' or 'B' or 'D':
		print('Please enter again(A(Attack1) or B(Attackk2) or D(Defence)):')

	
	if user_input == 'A':
		player_attack_value = player.attack()       #玩家的攻击值(简称：攻击）
		enemy_attack_value = enemy.attack()          #敌人的攻击值(简称：攻击）
		enemy.being_attack(player_attack_value)      #敌人所承受的攻击值是由玩家带来的
		enemy2.being_attack(player_attack_value)  
		player.being_attack(enemy_attack_value)      #玩家所承受的攻击值是由敌人带来的



	elif user_input == 'B':
		player_attack_value = player.attack()
		enemy_attack_value  = enemy.attack()
		enemy.being_attack2(player_attack_value)
		enemy2.being_attack2(player_attack_value)
		player.being_attack2(enemy_attack_value)


	elif user_input == 'D':                   #玩家选择防守
		enemy_attack_value = enemy.attack()*0.1   #因为是防守所以呢，就可以在原本的攻击值上乘于十分之一（也就是0.1）
		player.being_attack(enemy_attack_value)   #玩家要承担敌人攻击的数值



if player.not_dead():
	print("You win!")
else:
	print("You lose!")


	






'''
python Class19_GroupC8_0basic_hw.py
'''