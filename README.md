# CECS277-from-Lab03
📄 README.md
# Hangman Game 🎮

A simple command-line **Hangman** game written in Python.  
The player guesses letters to uncover a hidden 5-letter word before the stick figure is fully drawn.

---

## 📌 Features
- Randomly selects a word from a dictionary of 5-letter words.
- Displays a gallows that updates with each incorrect guess.
- Shows incorrect guesses, correct guesses, and remaining letters.
- Detects repeated guesses and prevents double-counting.
- Replay option after each game.

---

## 🗂 Project Structure


hangman/
│── hangman.py # Main game program
│── dictionary.py # List of 5-letter words
│── check_input.py # Helper functions for validated input
│── README.md # Project documentation


---

## ▶️ How to Play
1. Run the game:
   ```bash
   python hangman.py


A random 5-letter word is chosen.

Enter letters one by one:

Correct guesses reveal letters in the word.

Incorrect guesses draw more of the gallows.

You win if you guess all 5 letters before 6 mistakes.

You lose if the gallows is complete.

Play again? Just type Y when prompted.

📚 Requirements

Python 3.7+

No external libraries required (uses only built-in Python functions).

📝 Example Gameplay
-Hangman-

Incorrect selections: 
========
||/   |
||    
||    
||    

_ _ _ _ _

Remaining letters: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

Enter a letter: A
Correct!

_ A _ _ _

✨ Future Improvements

Support for words of different lengths (not just 5).

Difficulty modes (easy, medium, hard).

Score tracking across multiple rounds.

👩‍💻 Author

Gemma Truong
Project for class CECS277 lab


---
