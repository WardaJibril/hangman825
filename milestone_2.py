import random

word_list = ["kiwi", "raspberry","orange","mango", "pineapple"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = str(input("Enter a letter:"))
length_guess = len(guess)
if length_guess == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input")

