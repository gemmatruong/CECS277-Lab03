from entity import Entity
import random

class Enemy(Entity):
    """Extends entity - monster character that the hero encounters in the maze"""
    def __init__(self):
        # Randomize an enemy
        names = ["Goblin", "Vampire", "Ghoul", "Skeleton", "Zombie"]
        name = random.choice(names)
        max_hp = random.randint(4, 8)
        super().__init__(name, max_hp)
    
    def attack(self, entity):
        # Attack the opposing entity
        dmg = random.randint(1,4)
        entity.take_damage(dmg)
        return f"{self.name} attacks {entity.name} for {dmg} damage"
    