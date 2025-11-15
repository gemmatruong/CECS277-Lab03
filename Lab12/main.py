""" LAB #12
    11/12/2025
    Student 1: Thi, Truong
    Student 2: Udonna, Uchegbulam

    A program that uses the Decorator pattern to create a game that has the user add food 
    to their plate without going over the weight or area limit of a paper plate.
"""

from small_plate import SmallPlate
from large_plate import LargePlate
from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from green_beans import GreenBeans
from pie import Pie
import check_input

def examine_plate(p):
    '''display the description. Using [:-4] to not incude 'and' at the end'''
    print(p.description()[:-4])
    weight = p.weight()
    area = p.area()
    studiness = "Studiness: "
    space = "Space Available: "

    # If area or weight capacity is less than or equal to 0,
    # display a message for the type of failure, then return True
    if weight < 1 or area < 1:
        print("Your plate isn't big enough for this much food! Your food spills over the edge.")
        return True

    # Studiness
    if 1 <= weight <= 6:
        studiness += "Bending"
    elif 7 <= weight <= 12:
        studiness += "Weak"
    else:
        studiness += "Strong"
    
    # Space available
    if 1 <= area <= 20:
        space += "Tiny bit"
    elif 21 <= area <= 40:
        space += "Some"
    else:
        space += "Plenty"
    
    print(studiness)
    print(space)
    return False
    

def main():
    print("--Thanksgiving Dinner--")
    print("Serve yourself as much food as you like from the buffet,")
    print("but make sure that your plate will hold without spilling everywhere!")
    print("Choose a plate:")
    print("1. Small Sturdy Plate")
    print("2. Large Flimsy Plate")
    plate_choice = check_input.get_int_range(">> ",1,2)

    # Initialize the plate instance
    if plate_choice == 1:
        plate = SmallPlate()
    else:
        plate = LargePlate()
    
    full = False

    while not full:
        # Players are given options of food to add to their plate
        print()
        print("1. Turkey")
        print("2. Stuffing")
        print("3. Potatoes")
        print("4. Green Beans")
        print("5. Pie")
        print("6. Quit")
        food_choice = check_input.get_int_range(">> ",1,6)

        if food_choice == 6:    # Quit
            print(plate.description()[:-4])
            if plate.count() == 0:
                print("Oh no, you got nothing on your plate...")
            else:
                print(f"Good job! You made it to the table with {plate.count()} items.")
            print(f"There was still {plate.area()} square inches left on your plate.")
            print(f"Your plate could have held {plate.weight()} more ounces of food.")
            print("Don't worry, you can always go back for more. Happy Thanksgiving!")
            break
        elif food_choice == 1:  # Add Turkey
            plate = Turkey(plate)
        elif food_choice == 2:  # Add Stuffing
            plate = Stuffing(plate)
        elif food_choice == 3:  # Add Potatoes
            plate = Potatoes(plate)
        elif food_choice == 4:  # Add Green Beans
            plate = GreenBeans(plate)
        else:   # Add Pie
            plate = Pie(plate)
        
        # Call examine_plate() function to display hints
        full = examine_plate(plate)

if __name__ == "__main__":
    main()