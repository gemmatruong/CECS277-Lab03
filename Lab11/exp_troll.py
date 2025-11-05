from entity import Entity
import random

class ExpTroll(Entity):
    def __init__(self):
        super().__init__("Horrible Troll", random.randint(15,18))
    
    def melee_attack(self, enemy):
        dmg = random.randint(8,12)
        enemy.take_damage(dmg)
        return f"{self.name} crushes {enemy.name} for {dmg} damage"
