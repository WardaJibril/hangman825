# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

A description of the project:
# what it does, the aim of the project, and what you learned
The computer chooses a word from a pre-defined list and selects a word. the user is asked to guess a letter form that word.
# Installation instructions

# Usage instructions

# File structure of the project
The python file milestone_2 contains the lsit of words the computer chooses randomly from. Also, it asks for the user to guess a letter and checks the user input is a single alphabetical letter.

The python file milestone_3 conatains two functions. The first checks the guess of the user and the second asks for user input. the second function calls the first function.

The python file milestone_4 contains the hangman class. Within the hangman class, the functions from milestone_3 have beeen added to. The class asks for user input, chaecks if the input is correct. If the input is correct, it then checks if the input is in the word chosen by the computer. If the guess is correct, the number of letters left to guess is decreased by 1 and the letter replaces the '_' placeholder in the word. Then, th user my guess again. If the guess is incorrect, the number of lives decreases by 1 and the user my try again.
# License information
