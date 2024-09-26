# import a necessary modul
import random

# Welcoming to the game
print("**Welcome to Hangman Game**")

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

# Generate list that contain "-" based on the choosen word
blank_letter = []
for bl in chosen_word:
    blank_letter.append("_")
print(f"Here are the word that you should guess: \n{blank_letter}")

# Input a letter
letter_guessed = input("Gues a letter: ").lower()
replace_blank_letter = []
for letter in chosen_word:
    if letter_guessed == letter:
        replace_blank_letter += letter
    else:
        replace_blank_letter += "_"
print(replace_blank_letter)


