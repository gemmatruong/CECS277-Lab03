from entity import Entity
import random

class BegGoblin(Entity):
    def __init__(self):
        super().__init__("Goblin", random.randint(7,9))
    
    def melee_attack(self, enemy):
        dmg = random.randint(4,6)
        enemy.take_damage(dmg)
        return f"{self.name} bites {enemy.name} for {dmg} damage"
