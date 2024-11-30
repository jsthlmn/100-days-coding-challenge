# Import library
import random
from higher_lower_art import logo, vs
from higher_lower_data import data

def format_data(compare):
    """Format the data into printable format"""
    name = compare['name']
    description = compare['description']
    country = compare['country']
    return f"{name} a {description}, from {country}"

def game_compare(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

# Print logo
print(logo)
score = 0
game_continue = True

while game_continue:
    # Declare variable and generate a random data
    compare_A = random.choice(data)
    compare_B = random.choice(data)
    if compare_A == compare_B:
        compare_B = random.choice(data)

    # Format the data into printable format
    print(f"Compare A: {format_data(compare_A)}")
    print(vs)
    print(f"Againts B: {format_data(compare_B)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if the answer is correct
    is_correct = game_compare(guess, compare_A['follower_count'], compare_B['follower_count'])

    # Give user a feedback
    if is_correct:
        score += 1
        print(f"You're right, Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continue = False

