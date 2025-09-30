from die import Die

class Player:
    def __init__(self):
        self._dice = [Die(), Die(), Die()]
        self._dice.sort()
        self._points = 0
    
    def points(self):
        return self._points
    
    def roll_dice(self):
        for d in self._dice:
            d.roll()
        self._dice.sort()
    
    def has_pair(self):
        if self._dice[0] == self._dice[1] or self._dice[0] == self._dice[2] or self._dice[1] == self._dice[2]:
            self._points += 1
            return True
        return False
    
    def has_three_of_a_kind(self):
        if self._dice[0] == self._dice[1] == self._dice[2]:
            self._points += 3
            return True
        return False
    
    def has_series(self):
        if (self._dice[2] - self._dice[1]) == 1 and (self._dice[1] - self._dice[0]) == 1:
            self._points += 2
            return True
        return False
    
    def __str__(self):
        s = ""
        for i, d in enumerate(self._dice):
            s += "D" + str(i + 1) + "=" + str(d) + " "
        return s
    