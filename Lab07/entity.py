class Entity:
    """
    Represents a basic game entity with a name, health points (HP),
    and the ability to take damage.

    Attributes:
        _name (str): The name of the entity.
        _hp (int): The current health points of the entity.
        _max_hp (int): The maximum health points the entity can have.
    """
    def __init__(self, name, max_hp):
        self._name = name
        self._hp = max_hp
        self._max_hp = max_hp

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    def take_damage(self, dmg):
        temp = self._hp - dmg
        if temp < 0:
            self._hp = 0
        else:
            self._hp = temp
    def __str__(self):
        return f"{self.name}: {self.hp}/{self._max_hp}"
    