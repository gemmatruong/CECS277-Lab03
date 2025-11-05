from entity import Entity
import random

class BegTroll(Entity):
    def __init__(self):
        super().__init__("Troll", random.randint(8,10))
    
    def melee_attack(self, enemy):
        dmg = random.randint(5,9)
        enemy.take_damage(dmg)
        return f"{self.name} smashes {enemy.name} for {dmg} damage"
