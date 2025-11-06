from entity import Entity
import random

class ExpGoblin(Entity):
    """Extend from Entity - the hard Goblin that the factories construct."""
    def __init__(self):
        super().__init__("Angry Goblin", random.randint(12,15))
    
    def melee_attack(self, enemy):
        # randomize the damage (5-8), deal the damage to the enemy (the hero)
        # return a string describing the attack.
        dmg = random.randint(5,8)
        enemy.take_damage(dmg)
        return f"{self.name} slams {enemy.name} for {dmg} damage"
