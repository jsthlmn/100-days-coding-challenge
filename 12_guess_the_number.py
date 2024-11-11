from guess_the_number_art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0

if user_choice == 'easy':
    attempts = 10
elif user_choice == 'hard':
    attempts = 5
else:
    print("Invalid input, please type 'easy' or 'hard'")