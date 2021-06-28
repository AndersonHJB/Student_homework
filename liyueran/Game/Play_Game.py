# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 11:15 上午
# @Author  : AI悦创
# @FileName: Play_Game.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
# import random
from random import randint

class Creature():
	def __init__(self, hp):
		self.hp = hp
	
	def attack(self):
		# 我希望得到一个随机的数值
		attack_value = randint(0, 50)
		return attack_value
	
	def not_dead(self):
		if self.hp <= 0:
			return False
		return True
	
	def being_attack(self, attack_value):
		self.hp = self.hp - attack_value


player = Creature(100)
enemy = Creature(80)

while player.not_dead() and enemy.not_dead():
	user_input = input("Attack or Defence(A/D):").upper()
	
	if user_input == "A":
		player_attack_value = player.attack()
		enemy_attack_value = enemy.attack()
		
		enemy.being_attack(player_attack_value)
		player.being_attack(enemy_attack_value)
		
	elif user_input == "D":
		enemy_attack_value = enemy.attack()*0.1
		
		


