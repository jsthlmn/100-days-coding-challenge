import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
inpt_letters = int(input("How many letters would you like in your password? "))
inpt_symbols = int(input("How many symbols would you like? "))
inpt_numbers = int(input("How many numbers would you like? "))

pw_letter = ""
for letter in range(0, inpt_letters):
    num_items = len(letters)
    random_choice = random.randint(0, num_items -1)
    letter = letters[random_choice]
    pw_letter = pw_letter + letter
# print(pw_letter)

pw_symbol = ""
for symbol in range(0, inpt_symbols):
    num_items = len(symbols)
    random_choice = random.randint(0, num_items -1)
    symbol = symbols[random_choice]
    pw_symbol = pw_symbol + symbol
# print(pw_symbol)

pw_number = ""
for number in range(0, inpt_numbers):
    num_items = len(numbers)
    random_choice = random.randint(0, num_items -1)
    number = numbers[random_choice]
    pw_number = pw_number + number
# print(pw_number)

# ----------Easy Way-----------
# print(f"Your password is: {pw_letter}{pw_symbol}{pw_number}")
generated_password = pw_letter + pw_symbol + pw_number
print(f"Your password is: {generated_password}")


# ----------Hard Way-----------
# Make string into list
# generated_password_list = list(generated_password)
# random.shuffle(generated_password_list)

# Turn list into string

# generated_password_shuffle = ""
# for i in generated_password_list:
#     generated_password_shuffle = generated_password_shuffle + i
# print(f"Your password is: {generated_password_shuffle}")




# ---------OR---------
# Using random.choice

# password_list = []
# for letter in range(0, inpt_letters):
#     password_list.append(random.choice(letters))

# for symbol in range(0, inpt_symbols):
#     password_list += random.choice(symbols)

# for number in range(0, inpt_numbers):
#     password_list += random.choice(numbers)

# random.shuffle(password_list)

# password = ""
# for char in password_list:
#     password += char

# print(f"Your password is: {password}")
