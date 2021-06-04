import random
from sys import exit
import os
import time

#———————————————— class area————————————————>
class Creatrue():
	def __init__ (self,name,hp):
		self.name = name
		self.hp = hp

	def not_dead(self):
		if self.hp < 0:
			return False
		else:
			return True

	def being_attack(self,attack_value):
		self.hp=self.hp - attack_value

	def attack(self):#攻击选项的内部程序
		value = random.randint(10,50)
		return value

	def big_attack(self):#大招选项的内部程序
		hp_down = random.randint(5,20)
		self.hp = self.hp - hp_down
		value = random.randint(50,100)
		return value

	def treatment(self):#治愈选项的内部程序
		hp_up = random.randint(40,80)
		self.hp = self.hp + hp_up


	def show(self):
		print('{}的血量为{}'.format(self.name,self.hp))

	def attack_show(self):
		print('接下来每遇到一位敌人你有三种选择：（请务必认真阅读）')
		print('1.攻击：对敌方造成10~50的伤害值')
		print('2.治愈：给自己回复40~80的生命值')
		print('3.大招：给敌方造成50~100的伤害值，但是自身会损伤5~20的生命值')
		print('攻击（A） 治愈（H） 大招（R）')

#————————————————game first————————————————>
print('你好，我是本游戏的开发者坂Edge')
time.sleep(1)
print('欢迎来到对战游戏，在这个游戏中，你讲扮演Maker毕进行冒险')
time.sleep(1)
print('游戏过程中，你会遇到重重阻挠，但是希望你可以突破困难最终击败大魔王，赢得最后的胜利')
time.sleep(3)
os.system('cls')

#————————————————object show————————————————>
player = Creatrue('Maker毕',500)
enemy1 = Creatrue('小怪',100)
enemy2 = Creatrue('大魔王',500)

#————————————————game start————————————————>
player.attack_show()
time.sleep(15)
os.system('cls')
print('！！！遇到敌人！！！')
print('')
print('')

#————————————————while area with 小怪————————————————>
while player.not_dead() and enemy1.not_dead():
	player.show()
	enemy1.show()
	user_input = input('请选择: ')

	if user_input == 'A':
		player_attack_value = player.attack()
		enemy1_attack_value = player.attack()
		enemy1.being_attack(player_attack_value)
		player.being_attack(enemy1_attack_value)

	elif user_input == 'R':
		player_attack_value = player.big_attack()
		enemy1_attack_value = player.attack()
		enemy1.being_attack(player_attack_value)
		player.being_attack(enemy1_attack_value)

	elif user_input == 'H':
		player.treatment()
		enemy1_attack_value = player.attack()
		player.being_attack(enemy1_attack_value)

if player.not_dead():
	os.system('cls')
	print('小怪已被击败')
	print('！！！大魔王出现！！！')
	print('')
	print('')
else:
	os.system('cls')
	print('你已阵亡')
	exit()

#————————————————while area with 大魔王————————————————>
while player.not_dead() and enemy2.not_dead():
	player.show()
	enemy2.show()
	user_input = input('请选择: ')

	if user_input == 'A':
		player_attack_value = player.attack()
		enemy2_attack_value = player.attack()*1.5
		enemy2.being_attack(player_attack_value)
		player.being_attack(enemy2_attack_value)

	elif user_input == 'R':
		player_attack_value = player.big_attack()
		enemy2_attack_value = player.attack()*1.5
		enemy2.being_attack(player_attack_value)
		player.being_attack(enemy2_attack_value)

	elif user_input == 'H':
		player.treatment()
		enemy2_attack_value = player.attack()*1.5
		player.being_attack(enemy2_attack_value)

if player.not_dead():
	os.system('cls')
	print('恭喜你战胜了大魔王，赢得了本场游戏的胜利！')
else:
	os.system('cls')
	print('你已阵亡')
    
# 首先我在这恭喜你，你把我跟你说的已经全部在这个对话式游戏中体现出来了；
# 1.定义类做的不错；
# 2. 设定函数也做到了；
# 3.变量命名方式也更正了；
# 4.赋值符号左右加空格不错；
# 5.代码划分区域做的不错，继续保持；
# 但是，有这几点。
# 1.既然是个游戏，为什么不给玩家设定名称的机会？（不做示例）
# 2.函数代码逻辑顺序再加强一些；
# 3.代码有些冗余，可以学算法课提升，有兴趣私我。
# 4.继续加油哦！