import random

class Hangman:
    def __init__(self, num_lives,word_list):

        self.word = random.choice(word_list)

        # below is a list comprehension containing _ for each letter not yet guessed
        self.word_guessed = ['_' for _ in self.word]

        # num_letters is an integer of the number of unique letters in the word that have not been guessed yet
        self.num_letters = len(set(self.word))

        self.num_lives = num_lives

        self.word_list = word_list

        # list of guesses that have already been tried
        self.list_of_guesses = []

    def check_guess(self,guess):

        guess = self.guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            for i in range(len(self.word_guessed)):
                if self.word[i] == guess:
                    guess = self.word[i]
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print (f"Sorry, {guess} is not in the word. Try again.")
            print (f"You have {self.num_lives} lives left.")

    def ask_for_input(self):

        while True:
          self.guess = input("Guess a letter:")

          self.length_guess = len(self.guess)

          if not self.guess.isalpha() or self.length_guess != 1:
              print("Invalid letter. Please, enter a single alphabetical character.")

          elif self.guess in self.list_of_guesses:
              print("You already tried that letter!")           
          else:
              self.check_guess(self.guess)

          self.list_of_guesses.append(self.guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(num_lives,word_list)
    while True:
        if num_lives == 0:
            print("You lost!")
            break
        elif num_lives > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")

word_list = ["kiwi", "raspberry","orange","mango", "pineapple"]
play_game(word_list)

