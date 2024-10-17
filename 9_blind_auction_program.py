from art import logo

print(logo)
print("Welcome to the secret auction program.")

input_name = input("What is your name? ")
input_bid = input("What is your bid? ")

bid_data = []

def add_new_bid_data(name, bid):
    new_bid_dict = {}
    new_bid_dict['name']= name
    new_bid_dict['bid']= bid

    bid_data.append(new_bid_dict)

add_new_bid_data(input_name, input_bid)
print(bid_data)