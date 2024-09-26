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
length_of_word = len(chosen_word)
blank_letter = []
for _ in range(length_of_word):
    blank_letter.append("_")
print(f"Here are the word that you should guess: \n{blank_letter}")

# Condition to guess if there are still blank part
while "_" in blank_letter:
    # Input a letter
    letter_guessed = input("Gues a letter: ").lower()
    # Replace the blank with letter_guessed or "_"
    for position in range(length_of_word):
        letter = chosen_word[position]
        if letter_guessed == letter:
            blank_letter[position] = letter
    print(blank_letter)

    # -------OR--------
    # replace_blank_letter = []
    # for letter in chosen_word:
    #     if letter == letter_guessed:
    #         replace_blank_letter += letter_guessed
    #     else:
    #         replace_blank_letter += "_"
    # print(replace_blank_letter)
print("Great, you guessed all the letter")


# -------OR---------
# end_of_game = False
# while not end_of_game:
#     # Input a letter
#     letter_guessed = input("Gues a letter: ").lower()
#     # Replace the blank with letter_guessed or "_"
#     for position in range(length_of_word):
#         letter = chosen_word[position]
#         if letter_guessed == letter:
#             blank_letter[position] = letter
#     print(blank_letter)

#     # -------OR--------
#     # replace_blank_letter = []
#     # for letter in chosen_word:
#     #     if letter == letter_guessed:
#     #         replace_blank_letter += letter_guessed
#     #     else:
#     #         replace_blank_letter += "_"
#     # print(replace_blank_letter)

#     if "_" not in blank_letter:
#         end_of_game = True
#         print("Great, you guessed all the letter")

