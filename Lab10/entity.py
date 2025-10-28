import abc

class Entity(abc.ABC):
    """Abstract class - describes a character in the game."""
    def __init__(self, name, max_hp):
        # initializes each of the instance variables
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

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

    def heal(self):
        # restores the entity’s hp to max_hp.
        self._hp = self._max_hp

    def __str__(self):
        # override __str__ function
        return f"{self.name}\nHP: {self.hp}/{self._max_hp}"

    @abc.abstractmethod
    def attack(self, entity):
        pass