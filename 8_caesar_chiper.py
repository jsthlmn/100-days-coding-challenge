alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
options = input("Type 'encode' to encrypt, type 'decode' to decrypt! :")
message = input("Type your message: ").lower()
shift = int(input("Enter the shift number: "))

def caesar(text_input, shift_amount, user_option):
    if user_option == "encode":
        encrypted = ""
        for letter in text_input:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            encrypted += new_letter
        print(f"The encrypted messages is: {encrypted}")

        # ---------OR----------
        # Create an empty list called 'encrypted'
        # encrypted = []

        # # For each letter in the message that user inputs
        # for letter in text_input:
        #     # Find the position of the letter in the alphabet
        #     positions = alphabet.index(letter)
        #     # Shift the letter and add it to the 'encrypted' list
        #     encrypted += alphabet[positions + shift_amount]

        # # Convert the 'encrypted' list into a string
        # encrypted_string = ""
        # for j in encrypted:
        #     encrypted_string += j
        # print(f"The encrypted messages is: {encrypted_string}")

        # ---------OR----------
        # Using the join method
        # encrypted = "".join(encrypted)
        # print(encrypted)
        
    elif user_option == "decode":
        decrypted = ""
        for letter in text_input:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            decrypted += new_letter
        print(f"The decrypted messages is: {decrypted}")
    else:
        print("Invalid option, please choose 'encode' or 'decode'! ")

caesar(text_input=message, shift_amount=shift, user_option=options)