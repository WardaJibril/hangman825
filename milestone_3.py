def check_guess(guess):

    guess = guess.lower()

    if guess in word:
        print(f"Good guess!{guess}is in the word.")
    else:
        print (f"Sorry, {guess} is not in the word. Try again.")

def ask_user_input(guess):
    while True:
      guess = input("Guess a letter:")
      length_guess = len(guess)
      if not guess.isalpha() and length_guess != 1:
        print("Invalid letter. Please, enter a single alphabetical character.")
      else:
        break
    check_guess(guess)
