from die import Die

class Player:
    """ Represents a player in a dice game.

    A Player has three dice and earns points based on the outcome
    of rolling them. The scoring system is:
        - 3 of a kind = +3 points
        - Series of 3 consecutive numbers = +2 points
        - Pair (two dice showing the same number) = +1 point
    """
    def __init__(self):
        """ Constructs and sorts the list of three Die objects 
            and initializes the player’s points to 0.
        """
        self._dice = [Die(), Die(), Die()]
        self._dice.sort()
        self._points = 0
    
    def points(self):
        """
        Get property that returns the player’s current points.

        Returns:
            int: The total accumulated points.
        """
        return self._points
    
    def roll_dice(self):
        """
        Roll all three dice in the list and then sort the list.

        Side Effects:
            Updates the values of each die and rearranges them in ascending order.
        """
        for d in self._dice:
            d.roll()
        self._dice.sort()
    
    def has_pair(self):
        """
        Return True if two dice in the list have the same value.
        Increments the player’s points by 1 if a pair is found.

        Returns:
            bool: True if a pair is found, False otherwise.            
        """

        if self._dice[0] == self._dice[1] or self._dice[0] == self._dice[2] or self._dice[1] == self._dice[2]:
            self._points += 1
            return True
        return False
    
    def has_three_of_a_kind(self):
        """
        Return True if all three dice in the list have the same value.
        Increments the player’s points by 3 if three of a kind is found.

        Returns:
            bool: True if all three dice match, False otherwise.
            
        """
        if self._dice[0] == self._dice[1] == self._dice[2]:
            self._points += 3
            return True
        return False
    
    def has_series(self):
        """
        Return True if the values of the dice are in a sequence.
        Increments the player’s points by 2 if a series is found.

        Returns:
            bool: True if the dice form a series, False otherwise.
        """
        if (self._dice[2] - self._dice[1]) == 1 and (self._dice[1] - self._dice[0]) == 1:
            self._points += 2
            return True
        return False
    
    def __str__(self):
        """
        Return a string representation of the dice.

        Returns:
            str: A formatted string showing each die’s value.
        """
        s = ""
        for i, d in enumerate(self._dice):
            s += "D" + str(i + 1) + "=" + str(d) + " "
        return s
    