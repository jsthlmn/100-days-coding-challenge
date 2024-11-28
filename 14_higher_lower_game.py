# Import library
import random
from higher_lower_art import logo, vs
from higher_lower_data import data

# Declare variable
compare_A = random.choice(data)
compare_B = random.choice(data)

def game_compare():
    if compare_A['follower_count'] > compare_B['follower_count']:
        return 'A'
    else:
        return 'B'

def guess_answer(guess, answer, score):
    if guess == answer:
        print(logo)
        print(f"You're right, Current score: {score + 1}")
    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")

def game():
    game_over = False
    while not game_over:
        print(f"Compare A: {compare_A['name']}, {compare_A['description']}, from {compare_A['country']}")
        print(vs)
        print(f"Againts B: {compare_B['name']}, {compare_B['description']}, from {compare_B['country']}")
        guess = input("Who has more followers? Type 'A' or 'B': ")
        
        answer = game_compare()
        score = 0
        
        if guess == answer:
            print(logo)
            print(f"You're right, Current score: {score + 1}")
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

print(logo)
game()