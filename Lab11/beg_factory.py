from enemy_factory import EnemyFactory
from beg_goblin import BegGoblin
from beg_troll import BegTroll
import random

class BeginnerFactory(EnemyFactory):
    def create_random_enemy(self):
        enemy = random.choice([BegGoblin,BegTroll])
        return enemy()