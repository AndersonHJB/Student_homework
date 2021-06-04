#<-----------------导入数据库区域------------------->
import random
#<---------------------玩家输入区------------------------->

player_name = input('Please tell me your name:')
enemy_name1 = input('Please name your enemy：')    #给玩家提供一个扎小人的机会
enemy_name2 = 'Creep'   #顾及玩家体验，怪物2默认，避免重复输入的疲劳;如有需要也可以开放命名。

#<------------------类函数区域------------------------>
class Creature():
	def __init__(self,hp,attack_value,name):
		self.hp = hp
		self.attack_value = attack_value
		self.name = name

	def attack(self):
		attack_value = random.randint(0,50)
		return attack_value

	def being_attack(self,attack_value):
		self.hp = self.hp - attack_value

	def not_dead(self):
		if self.hp <= 0:
			return False
		else:
			return True

	def worrior(self):   #通过定义增加职业分类功能
		self.hp += 80
		self.attack_value -= 20

	def mega(self):
		self.hp += 10
		self.attack_value += 50

	def hunter(self):
		self.hp += 20
		self.attack_value += 20


	def show_status(self):
		print('{}\'s hp is{}.'.format(self.name,self.hp))


#<--------------------输出与调用区域------------------->

player = Creature(200,100,player_name)   
enemy = Creature(200,40,enemy_name1)   
enemy2 = Creature(180,20,enemy_name2)

#<---------------------角色---------------------------------->
user_charater = input('Please choose your character(W/M/H):')   #增加玩家选择职业的功能
if user_charater == 'W':
	player.worrior()     #调用函数实现职业区分

elif user_charater == 'M':
	player.mega()

elif user_charater == 'H':
	player.Hunter()
else:
	print('I don\'t understant. Please choose again...')

#<--------------------while循环区---------------------->

while player.not_dead() and enemy.not_dead(): 

	player.show_status()
	enemy.show_status()
	enemy2.show_status()


	user_input = input('Choose your action A/B/D (Attack/Attack twice/Defence):')
	
	
	if user_input == 'A':
		player_attack_value = player.attack()
		enemy_attack_value = enemy.attack()
		enemy.being_attack(player_attack_value)
		enemy2.being_attack(player_attack_value)  
		player.being_attack(enemy_attack_value)


	elif user_input == 'B':
		player_attack_value = player.attack()
		enemy_attack_value  = enemy.attack()
		enemy.being_attack(player_attack_value)
		enemy2.being_attack(player_attack_value)
		enemy.being_attack(player_attack_value)      #区别于A，B攻击敌人两次。
		enemy2.being_attack(player_attack_value)
		player.being_attack(enemy_attack_value)


	elif user_input == 'D':                   
		enemy_attack_value = enemy.attack()*0.1 
		player.being_attack(enemy_attack_value) 


	else:
		print('Please enter again(A(Attack1) or B(Attackk2) or D(Defence)):')



if player.not_dead():
	print("You win!")
else:
	print("You lose!")


#由于我们设想的血条涉及动态内容，来不及拓展相关知识，截止2/26 23：20尚未能实现。