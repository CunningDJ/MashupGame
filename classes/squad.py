import random
from classes.ninja import Ninja
from classes.brute import Brute
from classes.commando import Commando

class Squad:
    
	
	def __init__(self,size):
		soldierOptions = [Ninja,Commando,Brute]
    	
		self.size = size
		self.soldiers = []
		for item in range(1,self.size+1):
			self.soldiers.append(random.choice(soldierOptions)())
    
	def printSquad(self):
		for soldier in self.soldiers:
			soldier.printStats()

	
	def printSampleAttack(self):
		totalDmg=0
		commandoTotalDmg=0
		ninjaTotalDmg=0
		bruteTotalDmg=0
		
		totalComm = self.soldiers.count(Commando)
		totalNinja = self.soldiers.count(Ninja)
		totalBrute = self.soldiers.count(Brute)
		
		for soldier in self.soldiers:
			printString = "Soldier: {0}".format(soldier.soldierType)
			critRoll = random.random()
			dmg = 0
			if soldier.critChance >= critRoll:
				dmg = soldier.criticalHit * soldier.damage * soldier.speed
			else:
				dmg = soldier.damage * soldier.speed
			
			printString += " | Damage: {0:.2f}".format(dmg)
			print(printString)			# Individual player damage
			totalDmg+=dmg
			
			if isinstance(soldier, Ninja):
				ninjaTotalDmg+=dmg
				totalNinja+=1
			elif isinstance(soldier, Brute):
				bruteTotalDmg+=dmg
				totalBrute+=1
			elif isinstance(soldier, Commando):
				commandoTotalDmg+=dmg
				totalComm+=1
			
		
		print("")
		print("Total Damage: {0:.2f}".format(totalDmg))
		print("Total Commando Damage: {0:.2f}".format(commandoTotalDmg))
		print("Total Brute Damage: {0:.2f}".format(bruteTotalDmg))
		print("Total Ninja Damage: {0:.2f}".format(ninjaTotalDmg))
		
		
		
		
		print("")
		avgDmg = totalDmg/self.size
		print("Average Damage: {0:.2f}".format(avgDmg))
		
		
		
		print("Commandos: {} Ninjas: {} Brutes: {}".format(totalComm,totalNinja,totalBrute))
		print("")
		print("Average Commando Damage: {0:.2f}".format(commandoTotalDmg/totalComm))
		print("Average Brute Damage: {0:.2f}".format(bruteTotalDmg/totalBrute))
		print("Average Ninja Damage: {0:.2f}".format(ninjaTotalDmg/totalNinja))