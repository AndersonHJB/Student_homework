import random

class Creature():
	def __init__(self,hp,attack_value,name):
		self.hp=hp
		self.attack_value=attack_value
		self.name=name

	def attack(self):
		attack_value=random.randint(0,50)
		return attack_value

	def being_attack(self,attack_value):
		self.hp=self.hp-attack_value

	def not_dead(self):
		if self.hp<=0:
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

enemy=Creature(80,100,'Enemy')
player=Creature(100,100,'Bi')

user_charater=input('Please choose your character(W/M/H):')
if user_charater=='W':
	player.worrior()

elif user_charater=='M':
	player.mega()

elif user_charater=='H':
	player.Hunter()
else:
	print('I don\'t understant. Please choose again...')


while player.not_dead() and enemy.not_dead():
	player.show_status()
	enemy.show_status()

	user_input=input('Attack or Defence(A/D):')

	if user_input=='A':
		player_attack_value=player.attack()
		enemy_attack_value=enemy.attack()
		enemy.being_attack(player_attack_value)
		player.being_attack(enemy_attack_value)
	elif user_input=='D':
		enemy_attack_value=enemy.attack()*0.1
		player.being_attack(enemy_attack_value)

if player.not_dead():
	print('You win!')
else:
	print('You lose!')