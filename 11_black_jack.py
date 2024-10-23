# from black_jack_art import logo
import random

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

user = []
computer = []
is_game_over = False

for _ in range(2):
    user.append(deal_card())
    computer.append(deal_card())

user_score = calculate_score(user)
computer_score = calculate_score(computer)

print(f"Your cards: {user}, the current score is {user_score}")
print(f"Computer's first card: {computer[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True