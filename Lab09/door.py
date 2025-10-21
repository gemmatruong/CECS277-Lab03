import abc

class Door(abc.ABC):
    """ An interface """
    @abc.abstractmethod
    def examine_door(self):
        """Description of the door"""
        pass

    @abc.abstractmethod
    def menu_options(self):
        """Menu options that user can choose from when attempting to unlock the door"""
        pass

    @abc.abstractmethod
    def get_menu_max(self):
        """The number of options in the above menu"""
        pass

    @abc.abstractmethod
    def attempt(self, option):
        """Describing what the user attempted"""
        pass

    @abc.abstractmethod
    def is_unlocked(self):
        """Checks to see if the door was unlocked"""
        pass
    
    @abc.abstractmethod
    def clue(self):
        """The hint that is returned if the user was unsuccessful at their attempt"""
        pass

    @abc.abstractmethod
    def success(self):
        """The congratulatory message if the user was successful"""
        pass
    

    


