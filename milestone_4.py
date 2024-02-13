import random

class Hangman:
    def __init__(self, num_lives,word_list):

         # number of lives player has at the start of the game
        num_lives = 5

        # list of words for the computer to choose at random for user to guess
        word_list = ["kiwi", "raspberry","orange","mango", "pineapple"]

        self.word = random.choice(word_list)

        # below is a list comprehension containing _ for each letter not yet guessed
        self.word_guessed = ['_' for _ in self.word]

        # num_letters is an integer of the number of unique letters in the word that have not been guessed yet
        self.num_letters = len(set(self.word))

        self.num_lives = num_lives

        self.word_list = word_list

        # list of guesses that have already been tried
        self.list_of_guesses = []

    def check_guess (self):

        self.guess = self.guess.lower()

        if self.guess in self.word:
            print(f"Good guess! {self.guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == self.guess:
                    self.word[i] = self.guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print (f"Sorry, {self.guess} is not in the word. Try again.")
            print (f"You have {self.num_lives} lives left.")

    def ask_for_input(self):

        while True:
          self.guess = input("Guess a letter:")

          self.length_guess = len(self.guess)

          if not self.guess.isalpha() and self.length_guess != 1:
              print("Invalid letter. Please, enter a single alphabetical character.")

          elif self.guess in self.list_of_guesses:
              print("You already tried that letter!")
          else:
              self.check_guess(self.guess)

          self.list_of_guesses.append(self.guess)

# when calling class pass in num of lives and words to choose from
#hangman_game = Hangman(num_lives = 5, word_list = ["kiwi", "raspberry","orange","mango", "pineapple"])
#hangman_game.ask_for_input()

