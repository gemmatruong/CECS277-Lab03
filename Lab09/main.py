"""
    Student 1: Thi, Truong
    Student 2: Udonna, Uchegbulam

    Date: 10/22/2025

    A program that simulates an escape room by having the user open a series of three doors
    random chosen from several different types of doors.
"""

from basic_door import BasicDoor
from locked_door import LockedDoor
from combo_door import ComboDoor
import check_input
import random

def open_door(door):
    """ Create a loop to display the door's description, menu options, attempt's description, and congratulation (if applicable)
        It also gets the user selection to open the door.
        Arg: a Door object
        Return: NA
    """
    unlocked = False
    print(door.examine_door())

    while not unlocked:
        print(door.menu_options())
        user_choice = check_input.get_int_range("", 1, door.get_menu_max())
        print(door.attempt(user_choice))
        if door.is_unlocked():
            print(door.success())
            unlocked = True
        else:
            print(door.clue())

def main():
    print("Welcome to the Escape Room.")
    print("You must unlock 3 doors to escape...")
    for i in range(3):
        door_list = [BasicDoor(), LockedDoor(), ComboDoor()]
        door = random.choice(door_list)
        open_door(door)
        print()
    
    print("Congratulations! You escaped...this time.")

if __name__ == "__main__":
    main()