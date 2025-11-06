from enemy_factory import EnemyFactory
from exp_goblin import ExpGoblin
from exp_troll import ExpTroll
import random

class ExpFactory(EnemyFactory):
    """Extends from EnemyFactory to create a difficult enemy"""
    def create_random_enemy(self):
        # randomly construct and return one of the expert enemies
        enemy = random.choice([ExpGoblin, ExpTroll])
        return enemy()