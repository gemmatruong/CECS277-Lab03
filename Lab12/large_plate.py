from plate import Plate

class LargePlate(Plate):
    def description(self):
        ''' Returns a string dessription of the plate and what is on it'''
        return "Flimsy 12-inch paper plate with "

    def area(self):
        ''' Returns the area of the plate'''
        return 113

    def weight(self):
        '''  Returns the width of the plate'''
        return 24

    def count(self):
        ''' Returns 0 (ie. no items on the plate yet)'''
        return 0