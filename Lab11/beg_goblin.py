from entity import Entity
import random

class BegGoblin(Entity):
    """Extend from Entity - the easy Goblin that the factories construct."""
    def __init__(self):
        super().__init__("Goblin", random.randint(7,9))
    
    def melee_attack(self, enemy):
        # randomize the damage (4-6), deal the damage to the enemy (the hero)
        # return a string describing the attack.
        dmg = random.randint(4,6)
        enemy.take_damage(dmg)
        return f"{self.name} bites {enemy.name} for {dmg} damage"
