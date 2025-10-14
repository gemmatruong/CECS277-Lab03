import abc
import random

class Vehicle(abc.ABC):
    def __init__(self, name, initial, speed):
        self._name = name
        self._initial = initial
        self._speed = speed
        self._position = 0
        self._energy = 100

    @property
    def initial(self):
        return self._initial

    @property
    def position(self):
        return self._position

    @property
    def energy(self):
        return self._energy

    def fast(self, obs_loc):
        # Move the vehicle forward by a random amount given its speed +/-1
        if self.energy >= 5:
            spaces = random.randint(self._speed - 1, self._speed + 1)
            self._energy -= 5
            
            # check obstacle
            if (self.position + spaces) < obs_loc:
                self._position += spaces
                return f"{self._name} quickly moves {spaces} units"
            else:
                self._position = obs_loc
                self._energy -= 5
                return f"{self._name} CRASHED into an obstacle!"
        else:
            self._position += 1
            return f"{self._name} tries to move quickly, but is all out of energy!"


    def slow(self, obs_loc):
        # Move the vehicle by a random amount at half its speed
        #check obstacle
        spaces = random.randint(int(self._speed/2 - 1), int(self._speed/2 + 1))
        self._position += spaces
        return f"{self._name} slowly moves {spaces} units"

    def __str__(self):
        return f"{self._name}: [Position - {self.position}, Energy - {self.energy}]"

    @abc.abstractmethod
    def special_move(self, obs_loc):
        pass