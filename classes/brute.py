from classes.soldier import Soldier
import random
class Brute(Soldier):

	def __init__(self):
		self.soldierType = 'Brute'
		self.damage = random.randint(80,130) * 0.1
		self.speed = random.randint(1,4)
		self.criticalHit = random.randint(110,130) * 0.01
		self.critChance = random.randint(40,65) * 0.01