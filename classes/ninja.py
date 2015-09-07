from classes.soldier import Soldier
import random
class Ninja(Soldier):
    
    def __init__(self):
        self.soldierType = 'Ninja'
        self.damage = random.randint(50,90) * 0.1
        self.speed = random.randint(3,6)
        self.criticalHit = random.randint(110,120) * 0.01
        self.critChance = random.randint(50,80) * 0.01