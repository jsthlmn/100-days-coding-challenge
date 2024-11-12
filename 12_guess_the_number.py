from guess_the_number_art import logo
import random

# print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0
generate_random_number = random.randint(1, 100)
guess_number = generate_random_number

if user_choice == 'easy':
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number")
elif user_choice == 'hard':
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number")
else:
    print("Invalid input, please type 'easy' or 'hard'")


is_finished = False

while is_finished == False:
    user_guess = int(input("Make a guess: "))
    if user_guess == guess_number:
        print("Got it, you guessed the number!")
    elif user_guess > guess_number:
        print("Too high, guess again")
    elif user_guess < guess_number:
        print("Too low, guess again")