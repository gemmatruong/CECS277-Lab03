from dragon import Dragon
import random

class FlyingDragon(Dragon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self._swoops = 3
    
    def special_attack(self, hero):
        if self._swoops > 0:
            dmg = random.randint(5,8)
            hero.take_damage(dmg)
            self._swoops -= 1
            return f"{self.name()} swoops down and slashes you for {dmg} damage!"
        else:
            return f"{self.name()} tries to swoop down, but it's too exhausted to take flight."

    def __str__(self):
        return super().__str__() + f"\nSwoop attacks remaining: {self._swoops}"