import random

class Die:
    """
    Represents a single Die. Defaults to a 6-sided die.

    Attributes:
        sides (int): Number of sides on the die.
        value (int): The value of the rolled die.
    """

    def __init__(self, sides=6):
        """
        Initializes a Die object.

        Args:
            sides (int): The number of sides on the die. Defaults to 6.
        """
        self._sides = sides
        self._value = self.roll()

    def roll(self):
        """
        Rolls the die to set and return a random value.

        Returns:
            int: The randomly generated value between 1 and `sides`.
        """
        self._value = random.randint(1, self._sides)
        return self._value

    def __str__(self):
        """
        Returns the string representation of the die.

        Returns:
            str: The string form of the die's value.
        """
        return str(self._value)


    def __lt__(self, other):
        """
        Compares if this die's value is less than another die's value.

        Args:
            other (Die): Another die object.

        Returns:
            bool: True if self.value < other.value, otherwise False.
        """
        return self._value < other._value

    def __eq__(self, other):
        """
        Compares if this die's value is equal to another die's value.

        Args:
            other (Die): Another die object.

        Returns:
            bool: True if self.value == other.value, otherwise False.
        """
        return self._value == other._value
    
    def __sub__(self, other):
        """
        Subtracts the values of two dice.

        Args:
            other (Die): Another die object.

        Returns:
            int: The diffence of self.value and other.value.
        """
        return abs(self._value - other._value)