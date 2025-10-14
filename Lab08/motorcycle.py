from vehicle import Vehicle
import random

class Motorcycle(Vehicle):
    def slow(self, obs_loc):
        # Motorcycle moves by 75% of its speed rather than half
        # check obstacle
        spaces = random.randint(0.75*self._speed - 1, 0.75*self._speed + 1)
        if self.position + spaces < obs_loc:
            self._position += spaces
            return f"{self._name} slowly moves {spaces} units"
        else:
            self._position += spaces
            return f"{self._name} slowly dodges the obstacle and moves {spaces} units"

    def special_move(self, obs_loc):
        # 'wheelie' special ability: moving the motorcycle 2x its speed
        # check obstacle
        if self._energy >= 15:
            self._energy -= 15
            r = random.random() # 0.0 < r < 1.0
            if r < 0.75:
                spaces = random.randint(2*self._speed - 1, 2*self._speed + 1)
                if self.position + spaces > obs_loc:
                    self._position += spaces
                    return f"{self._name} pops a wheelie and moves {spaces} units"
                else:
                    self._position = obs_loc
                    return f"{self._name} tries to pop a wheelie, but CRASHED into an obstacle"
                    
            else:
                self._position += 1
                return f"{self._name} tries to pop a wheelie, but fall over and only move 1 space forward"
        else:
            self._position += 1
            return f"{self._name} tries to pop a wheelie, but is all out of energy"