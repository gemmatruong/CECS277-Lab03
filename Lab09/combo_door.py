from door import Door
import random

class ComboDoor(Door):
    def __init__(self):
        """Randomize the value to a number 1-10."""
        self._state = random.randint(1,10)

    def examine_door(self):
        """Returns a string description of the door."""
        return "You encounter a door with combination lock, you can spin the dial to a number 1-10."

    def menu_options(self):
        """ Returns a string of the menu options that user can choose from when
            attempting to unlock the door.
        """
        return "Enter # 1-10: "
    
    def get_menu_max(self):
        """Returns the number of options in the above menu."""
        return 10
    
    def attempt(self, option):
        """ Passes in the user’s selection from the menu. 
            Uses that value to update the attributes that are needed to determine 
            whether the user has unlocked the door.
            Returns a string describing what the user attempted.
        """
        self._input = option
        return f"You turn the dial to... {self._input}"
    
    def is_unlocked(self):
        """Checks to see if the door was unlocked, returns true if it is, false otherwise."""
        if self._state == self._input:
            return True
        else:
            return False
    
    def clue(self):
        """Returns the hint that is returned if the user was unsuccessful at their attempt."""
        if self._input < self._state:
            return "Try a higher value."
        if self._input > self._state:
            return "Try a lower value."
    
    def success(self):
        """Returns the congratulatory message if the user was successful."""
        if self.is_unlocked():
            return "Congratulations, you found the correct value and opened the door.."