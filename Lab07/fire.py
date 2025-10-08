from dragon import Dragon
import random

class FireDragon(Dragon):
    """
    Represents a fire dragon that inherits from the Dragon class.
    A FireDragon has a limited number of fire shots it can use for its
    special attack. When out of fire shots, the dragon can no longer
    perform its flame attack.

    Attribute: _fire_shot
    """
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self._fire_shot = 2
    
    def special_attack(self, hero):
        """
        It's an overridden fire attack – if the dragon has any
        fire_shots left, then apply a random amount of damage to the hero in the range 6-9,
        decrement the number of fire_shots.
        
        Return: a string with the description of the attack.
        Otherwise, do not deal any damage, and return a string describing the failure.
        """
        if self._fire_shot > 0:
            dmg = random.randint(6,9)
            hero.take_damage(dmg)
            self._fire_shot -= 1
            return f"{self.name} engulfs you in flames for {dmg} damage!"
        else:
            return f"{self.name} tries to spit fire at you but is all out of fire shots."

    def __str__(self):
        return super().__str__() + f"\nFire Shots remaining: {self._fire_shot}"