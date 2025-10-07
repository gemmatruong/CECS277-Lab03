from entity import Entity
import random

class Hero(Entity):
    def sword_attack(self, dragon):
        dmg = random.randint(1,6) + random.randint(1,6)
        dragon.take_damage(dmg)
        return f"You slash the {dragon.name()} with your sword for {dmg} damage."
    
    def arrow_attack(self, dragon):
        dmg = random.randint(1,12)
        dragon.take_damage(dmg)
        return f"You hit the {dragon.name()} with an arrow for {dmg} damage."
    