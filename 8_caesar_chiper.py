from caesar_art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(text_input, shift_amount, user_option):
#     final_text = ""
#     for char in text_input:
#         if char not in alphabet:
#             final_text += char
#         else:
#             position = alphabet.index(char)
#             if user_option == "encode":
#                 new_position = position + shift_amount
#             elif user_option == "decode":
#                 new_position = position - shift_amount
#             else:
#                 print("Invalid option. Please type 'encode' or 'decode'")
#             new_char = alphabet[new_position]
#             final_text += new_char
#     print(f"The {user_option}d message is: {final_text}")

# caesar(text_input=message, shift_amount=shift, user_option=options)

# ------------OR-----------------
def caesar(text_input, shift_amount, user_option):
    final_text = ""
    if user_option == "decode":
        shift_amount *= -1
    for char in text_input:
        if char not in alphabet:
            final_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            final_text += alphabet[new_position]
    print(f"The {user_option}d message is: {final_text}")

game_continue = True
while game_continue:
    options = input("Type 'encode' to encrypt, type 'decode' to decrypt! :")
    message = input("Type your message: ").lower()
    shift = int(input("Enter the shift number: "))
    shift = shift % 26

    caesar(text_input=message, shift_amount=shift, user_option=options)

    repeat_game = input("Type 'yes' if you want to go again, otherwise type 'no'. ").lower()
    if repeat_game == "no":
        game_continue = False
        print("Ok Goodbye")
    else:
        print("Invalid option. Please type 'yes' or 'no'.")

    