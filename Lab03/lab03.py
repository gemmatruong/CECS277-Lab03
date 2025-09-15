""" LAB #03
    09/10/2025
    Student 1: Thi, Truong
    Student 2: Udonna, Uchegbulam

    A program that plays a game of hangman with the user.
"""

import check_input
import random
from dictionary import words


def display_gallows(num_incorrect):
    """ Display the state of the hangman on the gallows based on the number of incorrect guesses.
        Input: num_incorrect - the number of incorrect guesses (0 to 6)
        Output: None
    """

    print("========")
    print("||/   |")

    if num_incorrect == 0:
        print("||")
        print("||")
        print("||")

    elif num_incorrect == 1:
        print("||    o")
        print("||")
        print("||")
        print("||")

    elif num_incorrect == 2:
        print("||    o")
        print("||    |")
        print("||")
        print("||")

    elif num_incorrect == 3:
        print("||    o")
        print("||    |")
        print("||   /")
        print("||")

    elif num_incorrect == 4:
        print("||    o")
        print("||    |")
        print("||   / \\")
        print("||")
    
    else:
        print("||   \\o")
        print("||    |")
        print("||   / \\")
        print("||")

def display_letters(letters):
    """ Display the letters in the list separated by spaces.
        Input: letters - a list of letters to display
        Output: None
    """
    for letter in letters:
        print(letter, end=" ")
    print("\n")

def get_letters_remaining(incorrect, correct):
    """ Create a list of remaining letters in the alphabet to choose from
        Input: incorrect - a list of incorrect letters
               correct - a list of correct letters
        Output: a list of remaining letters
    """
    remaining = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                 'Z']

    for letter in remaining[:]:
        if letter in incorrect or letter in correct:
            remaining.remove(letter)
    
    return remaining

def main():
    print("-Hangman-")
    print()
    
    play = True

    while play:
        target_word = random.choice(words).upper()
        incorrect_letters = []
        correct_letters = ['_', '_', '_', '_', '_']

        num_correct = 0
        num_incorrect = 0

        while num_correct < 5 and num_incorrect < 6:
            print("Incorrect selections:", end=" ")
            display_letters(incorrect_letters)

            display_gallows(num_incorrect)

            display_letters(correct_letters)

            remaining_letters = get_letters_remaining(incorrect_letters, correct_letters)
            print("Remaining letters:", end=" ")
            display_letters(remaining_letters)

            guess = check_input.get_char("Enter a letter: ")

            if guess in correct_letters or guess in incorrect_letters:
                print("You have already used that letter.")
            elif guess in target_word:
                print("Correct!")
                for i in range(len(target_word)):
                    if target_word[i] == guess:
                        correct_letters[i] = guess
                        num_correct += 1
                print()
            
            else:
                print("Incorrect!")
                print()
                incorrect_letters.append(guess)
                num_incorrect += 1
        
        if num_incorrect == 6:
            display_gallows(num_incorrect)
            print("You died!")
            print()
        else:
            print("You win!")
            print()
        
        play = check_input.get_yes_no("Play again (Y/N)? ")
        print()

if __name__ == "__main__":
    main()