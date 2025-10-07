from dragon import Dragon
import random

class FireDragon(Dragon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self._fire_shot = 2
    
    def special_attack(self, hero):
        if self._fire_shot > 0:
            dmg = random.randint(6,9)
            hero.take_damage(dmg)
            self._fire_shot -= 1
            return f"{self.name()} engulfs you in flames for {dmg} damage!"
        else:
            return f"{self.name()} tries to spit fire at you but is all out of fire shots."
    