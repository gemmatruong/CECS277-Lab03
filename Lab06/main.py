from player import Player
import check_input

def take_turn(player):
    player.roll_dice()
    print()
    print(player)
    if player.has_three_of_a_kind():
        print("You got 3 of a kind!")
    elif player.has_pair():
        print("You got a pair!")
    elif player.has_series():
        print("You got a series of 3!")
    else:
        print("Aww. Too Bad.")
    print(f"Score = {player.points()}")

def main():
    print("-Yahtzee-")
    player = Player()
    
    play = True
    while play:
        take_turn(player)
        play = check_input.get_yes_no("Play again? (Y/N): ")

        if not play:
            print()
            print("Game Over.")
            print(f"Final Score = {player.points()}")

if __name__ == "__main__":
    main()