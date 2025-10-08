from entity import Entity
import random

class Hero(Entity):
    """
    Represents a hero character that inherits from the Entity class.

    The Hero can perform different types of attacks on dragons,
    such as sword and arrow attacks. Each attack inflicts a random
    amount of damage within a specified range.
    """
    def sword_attack(self, dragon):
        """
        The method allows the dragon to take a random amount of damage in
        the range 2D6 (1-6 + 1-6). 
        Return: a string with the description of the attack.
        """
        dmg = random.randint(1,6) + random.randint(1,6)
        dragon.take_damage(dmg)
        return f"You slash the {dragon.name} with your sword for {dmg} damage."
    
    def arrow_attack(self, dragon):
        """
        The method allows the dragon to take a random amount of damage in
        the range e 1D12 (1-12).. 
        Return: a string with the description of the attack.
        """
        dmg = random.randint(1,12)
        dragon.take_damage(dmg)
        return f"You hit the {dragon.name} with an arrow for {dmg} damage."
    