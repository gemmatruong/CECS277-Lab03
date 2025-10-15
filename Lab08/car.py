from vehicle import Vehicle
import random

class Car(Vehicle):
    """ Represents a car - Inherit from Vehicle Class """
    def special_move(self, obs_loc):
        # 'nitro_boots' special ability: moving the car 1.5x its speed
        if self.energy >= 15:
            spaces = random.randint(int(1.5*self._speed - 1), int(1.5*self._speed + 1))
            self._energy -= 15

            # check obstacle
            if (self.position + spaces) < obs_loc:
                self._position += spaces
                return f"{self._name} uses nitro boost and moves {spaces} units"
            else:
                self._position = obs_loc
                return f"{self._name} tries to use nitro boost, but CRASHED into an obstacle"
        else:
            self._position += 1
            return f"{self._name} tries to use nitro boost, but is all out of energy!"
