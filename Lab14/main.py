""" LAB #14
    12/03/2025
    Student 1: Thi, Truong
    Student 2: Udonna, Uchegbulam

    Puppy Simulator - a program that has two basic functions: to feed or play with the puppy.
"""

import check_input
from puppy import Puppy

def main():
    ''' Construct a puppy object.
        Display a menu that allows the user to play with or feed the puppy.
        Display the puppy's reaction to the user's choice.
        Repeat until the user chooses to quit
    '''
    print("Congratulations on your new puppy!")
    my_puppy = Puppy()
    option = 0

    while option != 3:
        print()
        print("What would you like to do?")
        print("1. Feed the puppy")
        print("2. Play with the puppy")
        print("3. Quit")

        option = check_input.get_int_range("Enter choice: ", 1, 3)

        if option == 1:
            print(my_puppy.give_food())
        elif option == 2:
            print(my_puppy.throw_ball())
        
    print("Bye... Hope to see you soon!")

if __name__ == "__main__":
    main()