""" LAB #07
    10/08/2025
    Student 1: Thi, Truong
    Student 2: Udonna, Uchegbulam

    A program that creates a game where the user must defeat three dragons to pass the trials.
"""

from hero import Hero
from dragon import Dragon
from fire import FireDragon
from flying import FlyingDragon
import check_input
import random

def main():
    """
    Run the main game loop for the Dragon Training Game.

    The player must defeat three different dragons: 
    a regular Dragon, a FireDragon, and a FlyingDragon.
    
    The player can attack with either a sword or arrows, while
    dragons respond with random attacks. The game continues
    until either the hero's HP reaches 0 or all dragons are defeated.

    Inputs:
        User chooses:
            - Which dragon to attack.
            - Which weapon to use.
    
    Outputs:
        Prints battle updates, attack results, and win/loss messages.
    """

    # Ask for player name and create a Hero object with 50 HP
    player_name = input("What is your name, challenger?\n")
    player = Hero(player_name, 50)

    # Create a list of three dragons with different HP and attack types
    dragons = [Dragon("Deadly Nadder", 10), FireDragon("Gronckle", 15), FlyingDragon("Timberjack", 20)]

    print(f"Welcome to dragon training, {player_name}")
    print("You must defeat 3 dragons.")

    # Flag to track whether the player wins or loses
    win = True

    # Continue as long as the hero is alive and there are dragons left
    while player.hp > 0 and len(dragons) != 0:
        print()
        print(player) # Display current hero HP (e.g. "Hero: 35/50")

        # Display all dragons still alive
        remaining_dragons = len(dragons)
        for i in range(remaining_dragons):
            print(f"{i+1}. Attack {dragons[i]}")

        # Ask player which dragon to attack
        drg_to_attack = check_input.get_int_range("Choose a dragon to attack: ", 1, remaining_dragons)
        target = dragons[drg_to_attack - 1]

        print("Attack with:")
        print("1. Arrow (1 D12)")
        print("2. Sword (2 D6)")
        weapon = check_input.get_int_range("Enter weapon: ", 1, 2)

        if weapon == 1:
            print(player.arrow_attack(target))
        else:
            print(player.sword_attack(target))

        # If dragon's HP hits 0, it is defeated and removed from the list
        if target.hp == 0:
            print(f"You defeated the {target.name}!")
            dragons.remove(target)

        # If there are still dragons alive, one attacks back
        if dragons:
            random_drg = random.choice(dragons)
            random_attack = random.choice([random_drg.basic_attack, random_drg.special_attack])
            print(random_attack(player))

            # Check if the hero has been defeated
            if player.hp == 0:
                print("You are defeated!")
                win = False
    
    print()
    # Check if player win or not
    if win:
        print("Congratulations! You have defeated all 3 dragons, you have passed the trials.")
    else:
        print("Sorry... You lost!")

if __name__ == "__main__":
    main()