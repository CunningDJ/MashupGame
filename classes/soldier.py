class Soldier:
	import random

	def printStats(self):
		print("Type: {0} | Damage: {1:.1f} | Speed: {2} | Crit Hit: {3:.2f} | critChance: {4:.2f}".format(self.soldierType,self.damage,self.speed,self.criticalHit,self.critChance))