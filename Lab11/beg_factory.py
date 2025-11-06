from enemy_factory import EnemyFactory
from beg_goblin import BegGoblin
from beg_troll import BegTroll
import random

class BeginnerFactory(EnemyFactory):
    """Extends from EnemyFactory to create an easy enemy"""
    def create_random_enemy(self):
        # randomly construct and return one of the beginner enemies
        enemy = random.choice([BegGoblin,BegTroll])
        return enemy()