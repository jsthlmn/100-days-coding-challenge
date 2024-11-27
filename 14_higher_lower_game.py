# Import library
import random
from higher_lower_art import logo, vs
from higher_lower_data import data

# Declare variable
compare_A = random.choice(data)
compare_B = random.choice(data)

def game_compare(compare_A, compare_B):
    if compare_A['follower_count'] > compare_B['follower_count']:
        return 'A'
    else:
        return 'B'

def game():
    print(f"Compare A: {compare_A['name']}, {compare_A['description']}, from {compare_A['country']}")
    print(vs)
    print(f"Againts B: {compare_B['name']}, {compare_B['description']}, from {compare_B['country']}")
    print("Who has more followers? Type 'A' or 'B': ")