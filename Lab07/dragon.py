from entity import Entity
import random

class Dragon(Entity):
    def basic_attack(self, hero):
        dmg = random.randint(2,5)
        hero.take_damage(dmg)
        return f"{self.name()} smashes you with its tail for {dmg} damage!"
    def special_attack(self, hero):
        dmg = random.randint(3,7)
        hero.take_damage(dmg)
        return f"{self.name()} slashes you with its claws for {dmg} damage!"
    