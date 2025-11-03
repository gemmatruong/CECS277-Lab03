import abc

class Entity(abc.ABC):
    """Abstract class - describes a character in the game."""
    def __init__(self, name, hp):
        # initializes each of the instance variables
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    def take_damage(self, dmg):
        # subtracts the dmg from the hp, but does not allow the hp to go below 0.
        temp = self._hp - dmg
        if temp < 0:
            self._hp = 0
        else:
            self._hp = temp

    def __str__(self):
        # override __str__ function
        return f"{self.name} HP: {self.hp}"

    @abc.abstractmethod
    def melee_attack(self, enemy):
        pass