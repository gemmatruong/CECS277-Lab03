import abc
from plate import Plate

class PlateDecorator(Plate, abc.ABC):
    def __init__(self, p):
        ''' Pass in the plate p and assign it to the _plate attribute'''
        self._plate = p
    
    def description(self):
        ''' Returns a string dessription of the plate and what is on it'''
        return self._plate.description()
    
    def area(self):
        ''' Returns the remaining square inches the plate can hold'''
        return self._plate.area()
    
    def weight(self):
        ''' Returns the remaining number of ounces the plate can hold '''
        return self._plate.weight()
    
    def count(self):
        ''' Returns the number of food items the plate is current holding'''
        return self._plate.count()