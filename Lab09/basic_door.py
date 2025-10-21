from door import Door
import random

class BasicDoor(Door):
    def __init__(self):
        """Randomizes the initial state of the door (push or pull)."""
        self._state = random.randint(1,2)
    
    def examine_door(self):
        """Returns a string description of the door."""
        return "You encounter a basic door, you can either push it or pull it to open."
    
    def menu_options(self):
        """ Returns a string of the menu options that user can choose from when
            attempting to unlock the door.
        """
        return "1. Push\n2. Pull"
    
    def get_menu_max(self):
        """Returns the number of options in the above menu."""
        return 2
    
    def attempt(self, option):
        """ Passes in the user’s selection from the menu. 
            Uses that value to update the attributes that are needed to determine 
            whether the user has unlocked the door.
            Returns a string describing what the user attempted.
        """
        self._input = option
        if option == 1:
            return "You push the door."
        else:
            return "You pull the door."
    
    def is_unlocked(self):
        """Checks to see if the door was unlocked, returns true if it is, false otherwise."""
        if self._input == self._state:
            return True
        else:
            return False
    
    def clue(self):
        """Returns the hint that is returned if the user was unsuccessful at their attempt."""
        if not self.is_unlocked():
            return "Try the other way."
    
    def success(self):
        """Returns the congratulatory message if the user was successful."""
        if self.is_unlocked():
            return "Congratulations, you opened the door."