from vehicle import Vehicle
import random

class Truck(Vehicle):
    """ Represents a truck - Inherit from Vehicle Class """
    def special_move(self, obs_loc):
        # 'rams' special ability: moving the truck forward by 2x its speed
        # check obstacle
        if self.energy >= 15:
            spaces = random.randint(2*self._speed - 1, 2*self._speed + 1)
            self._energy -= 15
            self._position += spaces

            # check obstacle
            if self.position < obs_loc:
                return f"{self._name} rams forward {spaces} units!"
            else:
                return f"{self._name} rams into an obstacle, bashes through it {spaces} units!"
        else:
            self._position += 1
            return f"{self._name} tries to ram forward, but is all out of energy!"