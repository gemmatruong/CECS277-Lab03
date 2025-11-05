import check_input
import random
from beg_factory import BeginnerFactory
from exp_factory import ExpFactory
from hero import Hero

def main():
    print("Monster Trials")
    player_name = input("What is your name? ")

    player = Hero(player_name, 25)

    monsters = [BeginnerFactory().create_random_enemy(), 
                BeginnerFactory().create_random_enemy(), 
                ExpFactory().create_random_enemy()]

    die = False
    win = False


    while (not die) and (not win):
        # Ask player to choose a monster to attack
        print()
        print("Choose an enemy to attack:")
        for i, mon in enumerate(monsters):
            print(f"{i+1}. {mon}")
        opp_index = check_input.get_int_range("Enter choice: ",1,(len(monsters))) - 1
        opponent = monsters[opp_index]
        
        # Ask player to choose a weapon to attack
        print()
        print(player)
        print("1. Sword Attack")
        print("2. Arrow Attack")
        weapon = check_input.get_int_range("Enter choice: ", 1, 2)

        # Attack the monster with the selected weapon
        print()
        print(player.melee_attack(opponent))

        # If the monster is still alive, counterattacks.
        if opponent.hp > 0:
            print(opponent.melee_attack(player))
        else:
            print(f"You have slain the {opponent.name}")
            monsters.remove(opponent)
        
        # End game if player deafeated all 3 monster or player died
        if (len(monsters) == 0):
            win = True
            print("\nCongratulations! You defeated all three monsters!")
        if player.hp == 0:
            die = True
            print("\nYou died. Good luck next time!")
    print("Game Over!")

if __name__ == "__main__":
    main()