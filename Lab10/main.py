"""
    Student 1: Thi, Truong
    Student 2: Udonna, Uchegbulam

    Date: 10/29/2025

    A program that  allows the user to wander through a haunted dungeon maze and fight
    monsters that they encounter as they explore.
"""

from hero import Hero
from enemy import Enemy
from map import Map
import check_input
import random
    

def main():
    player_name = input("What is your name, traveler? ")
    
    # Initialize hero and map object
    player = Hero(player_name)
    game_map = Map()
    game_map.reveal(player.loc)

    die = False
    finish = False

    # Loop until the player reaches finish or dies.
    while not (die or finish):
        print()
        print(player)
        print(game_map.show_map(player.loc))

        # Display menu and get player choice
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        print("5. Quit")
        choice = check_input.get_int_range("Enter choice: ", 1, 5)

        if choice == 1: # Go North
            move = player.go_north()
        elif choice == 2: # Go South
            move = player.go_south()
        elif choice == 3: # Go East
            move = player.go_east()
        elif choice == 4: # Go West
            move = player.go_west()
        else:
            print("You chose to leave! Bye...")
            break

        if move == 'o':
            print("You cannot go that way...")
            continue

        game_map.reveal(player.loc)

        if move == "m": # monster
            monster = Enemy()
            print(f"You encounter a {monster}")
            
            # Loop until the player choose to run away or kill the monster
            while True:
                print(f"1. Attack {monster.name}\n2. Run Away")
                action = check_input.get_int_range("Enter choice: ", 1, 2)
                
                if action == 1: # Attack the monster
                    print(player.attack(monster))
                    
                    # Check if monster's still alive
                    if monster.hp > 0:
                        print(monster.attack(player))
                    else: # Monster is dead
                        print(f"You have slain a {monster.name}")
                        game_map.remove_at_loc(player.loc)
                        break
                    
                    # If player's hp is zero, player loses. 
                    if player.hp == 0:
                        print("You died!")
                        die = True
                        break

                else:   # Run away
                    run = False

                    # Loop until randomly choose a valid direction
                    while not run:
                        direction = random.choice(['n', 's', 'e', 'w'])
                        if direction == 'n': # north
                            result = player.go_north()
                        elif direction == 's': # south
                            result = player.go_south()
                        elif direction == 'e': # east
                            result = player.go_east()
                        elif direction == 'w': # west
                            result = player.go_west()

                        # only move if it's not out of bounds ('o')
                        if result != 'o':
                            print(f"You ran away!")
                            game_map.reveal(player.loc)
                            run = True
                        else:
                            # try another random direction
                            continue
                    break
        elif move == 'n': # nothing
            print("There is nothing here...")
        elif move == 's': # start
            print("You are back at the start!")
        elif move == 'i': # item room
            print("You found a Health Potion! You drink it to restore your health.")
            game_map.remove_at_loc(player.loc)
            player.heal()
        else: # finish
            print("Congratulations! You found the exit.")
            finish = True
    print("Game over!")

if __name__ == "__main__":
    main()