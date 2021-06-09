# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 10:35 上午
# @Author  : AI悦创
# @FileName: text_game.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
# 游戏名称：主角打怪-文字游戏
# 1. 一个玩家、一个敌人
# 2. 敌人和玩家互相攻击
# 3. 玩家可以选择攻击也可以选择防守，防守的时候敌人也会攻击，防守受到攻击值：十分之一
# 4. 攻击值：都是随机：random

import random


class Creature(object):
	def __init__(self, hp, name):
		self.hp = hp
		self.name = name
		
	def attack(self):
		"""
		我希望得到一个随机的攻击值
		:return:
		"""
		attack_value = random.randint(0, 50)
		return attack_value
	
	def not_dead(self):
		if self.hp <= 0:
			return False
		else:
			return True
	
	def being_attack(self, attack_value):
		self.hp -= attack_value
	
	def show_status(self):
		# print(self.hp)
		print("{}' hp is {}.".format(self.name, self.hp))
		
	
"""
player:玩家
enemy:敌人
"""
player = Creature(100, "AI悦创")
enemy = Creature(80, "Enemy")

while player.not_dead() and enemy.not_dead():
	player.show_status()
	enemy.show_status()
	user_input = input("Attack or Defence(A/D):").upper()
	if user_input == "A":
		"""获取攻击值"""
		player_attack_value = player.attack()
		enemy_attack_value = enemy.attack()
		"""受到攻击"""
		enemy.being_attack(player_attack_value)
		player.being_attack(enemy_attack_value)
	elif user_input == "D":
		enemy_attack_value = enemy.attack()*0.1
		player.being_attack(enemy_attack_value)

if player.not_dead():
	print("You Win!")
else:
	print("You Lose!")