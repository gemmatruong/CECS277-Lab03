from entity import Entity
import random

class ExpTroll(Entity):
    """Extend from Entity - the hard Troll that the factories construct."""
    def __init__(self):
        super().__init__("Horrible Troll", random.randint(15,18))
    
    def melee_attack(self, enemy):
        # randomize the damage (8-12), deal the damage to the enemy (the hero)
        # return a string describing the attack.
        dmg = random.randint(8,12)
        enemy.take_damage(dmg)
        return f"{self.name} crushes {enemy.name} for {dmg} damage"
