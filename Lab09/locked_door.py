from door import Door
import random

class LockedDoor(Door):
    def __init__(self):
        """Randomizes the location of the key."""
        self._state = random.randint(1,3)

    def examine_door(self):
        """Returns a string description of the door."""
        return "You encounter a locked door, the key is hidden nearby, you can look around for the key.."
    
    def menu_options(self):
        """ Returns a string of the menu options that user can choose from when
            attempting to unlock the door.
        """
        return "1. Look under the mat.\n2. Look under the flower pot.\n3. Look under the fake rock."
    
    def get_menu_max(self):
        """Returns the number of options in the above menu."""
        return 3
    
    def attempt(self, option):
        """ Passes in the user’s selection from the menu. 
            Uses that value to update the attributes that are needed to determine 
            whether the user has unlocked the door.
            Returns a string describing what the user attempted.
        """
        self._input = option
        if option == 1:
            return "You look for the key under the mat."
        elif option == 2:
            return "You look for the key under the flower pot."
        else:
            return "You look for the key under the fake rock."
    
    def is_unlocked(self):
        """Checks to see if the door was unlocked, returns true if it is, false otherwise."""
        if self._state == self._input:
            return True
        else:
            return False
    
    def clue(self):
        """Returns the hint that is returned if the user was unsuccessful at their attempt."""
        if not self.is_unlocked():
            return "Look somewhere else."
    
    def success(self):
        """Returns the congratulatory message if the user was successful."""
        if self.is_unlocked():
            return "Congratulations, you found the key and opened the door."