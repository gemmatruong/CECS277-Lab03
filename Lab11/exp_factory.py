from enemy_factory import EnemyFactory
from exp_goblin import ExpGoblin
from exp_troll import ExpTroll
import random

class ExpFactory(EnemyFactory):
    def create_random_enemy(self):
        enemy = random.choice([ExpGoblin, ExpTroll])
        return enemy()