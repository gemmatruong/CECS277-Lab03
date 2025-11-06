from entity import Entity
import random

class BegTroll(Entity):
    """Extend from Entity - the easy Troll that the factories construct."""
    def __init__(self):
        super().__init__("Troll", random.randint(8,10))
    
    def melee_attack(self, enemy):
        # randomize the damage (5-9), deal the damage to the enemy (the hero)
        # return a string describing the attack.
        dmg = random.randint(5,9)
        enemy.take_damage(dmg)
        return f"{self.name} smashes {enemy.name} for {dmg} damage"
