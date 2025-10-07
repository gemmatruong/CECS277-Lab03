""" LAB #06
    09/29/2025
    Student 1: Thi, Truong
    Student 2: Udonna, Uchegbulam

    A program that creates a dice game that awards the user points for a pair, three-of-a-kind, or a series.
"""


from player import Player
import check_input

def take_turn(player):
    """ Play one turn for the given player.

    This function roll the player’s dice, display the dice, check for and display any win
    types (pair, series, three-of-a-kind), and display the updated score

    Args:
        player: An object representing the player.
    """
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