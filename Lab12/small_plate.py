from plate import Plate

class SmallPlate(Plate):
    def description(self):
        ''' Returns a string dessription of the plate and what is on it'''
        return "Sturdy 10-inch paper plate with "

    def area(self):
        ''' Returns the area of the plate'''
        return 78

    def weight(self):
        '''  Returns the width of the plate'''
        return 32

    def count(self):
        ''' Returns 0 (ie. no items on the plate yet)'''
        return 0