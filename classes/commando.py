from classes.soldier import Soldier
import random
class Commando(Soldier):
     
    def __init__(self):
        self.soldierType = 'Commando'
        self.damage = random.randint(60,100) * 0.1
        self.speed = random.randint(2,5)
        self.criticalHit = random.randint(110,150) * 0.01
        self.critChance = random.randint(20,40) * 0.01