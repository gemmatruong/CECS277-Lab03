from entity import Entity
import random

class ExpGoblin(Entity):
    def __init__(self):
        super().__init__("Angry Goblin", random.randint(12,15))
    
    def melee_attack(self, enemy):
        dmg = random.randint(5,8)
        enemy.take_damage(dmg)
        return f"{self.name} slams {enemy.name} for {dmg} damage"
