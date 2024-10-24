from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids_data = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of {highest_bid}")

while not bidding_finished:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bids_data[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")

    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids_data)