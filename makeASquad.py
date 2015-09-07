from classes.soldier import Soldier
from classes.brute import Brute
from classes.ninja import Ninja
from classes.commando import Commando
from classes.squad import Squad

class main:
    
	def main():
		
		numSoldiers = int(input("How many members in your squad? "))
		theSquad = Squad(numSoldiers)
		theSquad.printSquad()
		while True:
			attack = False 
			print()
			response = input("Print a sample attack (y/n)? Type DONE to finish: ")
			if response == 'y' or response == 'Y':
				attack = True
			elif response == 'n' or response == 'N':
				attack = False
				continue
			elif response == 'DONE':
				break
			
			if(attack):
				theSquad.printSampleAttack()
				
		print("Program complete.")

		
	main()