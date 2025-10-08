from dragon import Dragon
import random

class FlyingDragon(Dragon):
    """
    Represents a flying dragon that inherits from the Dragon class.
    A FlyingDragon has a limited number of swoops it can use for its
    special attack. When out of swoops, the dragon can no longer
    perform its swoop attack.

    Attribute: _swoops
    """
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self._swoops = 3
    
    def special_attack(self, hero):
        """
        It's an overridden swoop attack – if the dragon has any
        swoops left, then apply a random amount of damage to the hero in the range 5-8,
        decrement the number of swoops.
        
        Return: a string with the description of the attack.
        Otherwise, do not deal any damage, and return a string describing the failure.
        """
        if self._swoops > 0:
            dmg = random.randint(5,8)
            hero.take_damage(dmg)
            self._swoops -= 1
            return f"{self.name} swoops down and slashes you for {dmg} damage!"
        else:
            return f"{self.name} tries to swoop down, but it's too exhausted to take flight."

    def __str__(self):
        return super().__str__() + f"\nSwoop attacks remaining: {self._swoops}"