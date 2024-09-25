# import a necessary modul
import random

# Welcoming to the game
print("Welcom to Hangman Game")

# Set a variable
word_list = ["lion", "elephant", "zebra", "monkey", "ant"]

# Generate a random word from word_list
length_of_list = len(word_list)
random_choice = random.randint(0, length_of_list -1)
chosen_word = word_list[random_choice]

# --------OR----------
# Using random choice
# chosen_word = random.choice(word_list)

print(chosen_word)

# Input a letter
letter_guessed = input("Gues a letter: ")
for cw in chosen_word:
    if letter_guessed == cw:
        print("Right")
    else:
        print("Wrong")
