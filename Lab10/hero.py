from entity import Entity
from map import Map
import random

class Hero(Entity):
    """Extends entity - the user’s character """
    def __init__(self, name):
        super().__init__(name, max_hp = 25)
        self._loc = [0,0]
    
    @property
    def loc(self):
        return self._loc
    
    def attack(self, entity):
        # Attack the opposing enemy
        dmg = random.randint(2,5)
        entity.take_damage(dmg)
        return f"{self.name} attacks a {entity.name} for {dmg} damage"
    
    def go_north(self):
        # Update row: self._loc[0] - 1
        # If that location is within the bounds

        game_map = Map()
        new_row = self._loc[0] - 1
        if 0 <= new_row < len(game_map):
            self._loc[0] = new_row
            return game_map[self._loc[0]][self._loc[1]]
        else:
            return 'o'
    
    def go_south(self):
        # Update row: self._loc[0] + 1
        # If that location is within the bounds
        
        game_map = Map()
        new_row = self._loc[0] + 1
        if 0 <= new_row < len(game_map):
            self._loc[0] = new_row
            return game_map[self._loc[0]][self._loc[1]]
        else:
            return 'o'
    
    def go_east(self):
        # Update row: self._loc[1] + 1
        # If that location is within the bounds
        
        game_map = Map()
        new_col = self._loc[1] + 1
        if 0 <= new_col < len(game_map):
            self._loc[1] = new_col
            return game_map[self._loc[0]][self._loc[1]]
        else:
            return 'o'
    
    def go_west(self):
        # Update row: self._loc[1] - 1
        # If that location is within the bounds
        
        game_map = Map()
        new_col = self._loc[1] - 1
        if 0 <= new_col < len(game_map):
            self._loc[1] = new_col
            return game_map[self._loc[0]][self._loc[1]]
        else:
            return 'o'
