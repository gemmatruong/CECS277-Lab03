from entity import Entity
import random

class Hero(Entity):
    """
    Represents a hero character that inherits from the Entity class.

    The Hero can perform different types of attacks on enemy,
    such as melee attack and ranged attack. Each attack inflicts a random
    amount of damage within a specified range.
    """
    def melee_attack(self, enemy):
        """
        The method allows the enemy to take a random amount of damage in
        the range 2D6 (1-6 + 1-6). 
        Return: a string with the description of the attack.
        """
        dmg = random.randint(1,6) + random.randint(1,6)
        enemy.take_damage(dmg)
        return f"{self.name} slashes the {enemy.name} with a sword for {dmg} damage."
    
    def ranged_attack(self, enemy):
        """
        The method allows the enemy to take a random amount of damage in
        the range e 1D12 (1-12).. 
        Return: a string with the description of the attack.
        """
        dmg = random.randint(1,12)
        enemy.take_damage(dmg)
        return f"{self.name} pierces the {enemy.name} with an arrow for {dmg} damage."
    