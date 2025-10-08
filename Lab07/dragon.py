from entity import Entity
import random

class Dragon(Entity):
    """
    Represents a dragon enemy that inherits from the Entity class.
    The Dragon can perform both basic and special attacks on a hero.
    Each attack deals a random amount of damage within a defined range.
    """
    def basic_attack(self, hero):
        """
        This is tail attack – the hero takes a random amount of
        damage in the range 2-5. 
        Return: a string with the description of the attack.
        """
        dmg = random.randint(2,5)
        hero.take_damage(dmg)
        return f"{self.name} smashes you with its tail for {dmg} damage!"
    def special_attack(self, hero):
        """
        This is claw attack – the hero takes a random amount of
        damage in the range 3-7. 
        Return: a string with the description of the attack.
        """
        dmg = random.randint(3,7)
        hero.take_damage(dmg)
        return f"{self.name} slashes you with its claws for {dmg} damage!"
    