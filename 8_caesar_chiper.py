alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
options = input("Type 'encode' to encrypt, type 'decode' to decrypt! :")
message = input("Type your message: ").lower()
shift = int(input("Enter the shift number: "))

def encrypt(messages_input, shifts_amount):
    encrypted = ""
    for letter in messages_input:
        position = alphabet.index(letter)
        new_position = position + shifts_amount
        new_letter = alphabet[new_position]
        encrypted += new_letter
    print(f"The encrypted messages is: {encrypted}")

encrypt(messages_input=message, shifts_amount=shift)

# ---------OR----------

# def encrypt(messages_input, shifts_amount):
#     # Create an empty list called 'encrypted'
#     encrypted = []

#     # For each letter in the message that user inputs
#     for letter in messages_input:
#         # Find the position of the letter in the alphabet
#         positions = alphabet.index(letter)
#         # Shift the letter and add it to the 'encrypted' list
#         encrypted += alphabet[positions + shifts_amount]

#     # Convert the 'encrypted' list into a string
#     encrypted_string = ""
#     for j in encrypted:
#         encrypted_string += j
#     print(f"The encrypted messages is: {encrypted_string}")

#     # ---------OR----------
#     # Using the join method
#     # encrypted = "".join(encrypted)
#     # print(encrypted)

# encrypt(messages_input=message, shifts_amount=shift)