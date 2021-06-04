#<-----------------导入数据库区域------------------->
import random
#<---------------------玩家输入区------------------------->

user_player_name1 = input('请设定玩家名称：')
user_enemy_name2 = input('请设定敌人名称：')
user_enemy_name3 = input('请设定敌人名称：')

#<------------------类函数区域------------------------>
class Creature():
	def __init__(self,hp,attack_value,name):
		self.hp = hp
		self.attack_value = attack_value
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

	def not_dead(self):
		if self.hp <= 0:
			return False
		else:
			return True

	def worrior(self):
		self.hp+=80
		self.attack_value-=20

	def mega(self):
		self.hp+=10
		self.attack_value+=50

	def hunter(self):
		self.hp+=20
		self.attack_value+=20


	def show_status(self):
		print('{}\'s hp is{}.'.format(self.name,self.hp))


#<--------------------输出与调用区域------------------->

player = Creature(100,100,user_player_name1)   #②如果需要填入初始值的话，那我们就是需要在class（类）里面提前定义这个值。/预设的地方。
enemy = Creature(80,100,user_enemy_name2)   #②如果需要填入初始值的话，那我们就是需要在class（类）里面提前定义这个值。/预设的地方
enemy2 = Creature(80,100,user_enemy_name3)

#<---------------------角色---------------------------------->
user_charater=input('Please choose your character(W/M/H):')
if user_charater=='W':
	player.worrior()

elif user_charater=='M':
	player.mega()

elif user_charater=='H':
	player.Hunter()
else:
	print('I don\'t understant. Please choose again...')

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