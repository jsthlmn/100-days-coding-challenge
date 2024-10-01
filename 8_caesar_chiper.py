alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
options = input("Type 'encode' to encrypt, type 'decode' to decrypt! :")
message = input("Type your message: ").lower()
shift = int(input("Enter the shift number: "))

# def caesar(text_input, shift_amount, user_option):
#     final_text = ""
#     for letter in text_input:
#         position = alphabet.index(letter)
#         if user_option == "encode":
#             new_position = position + shift_amount
#         elif user_option == "decode":
#             new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         final_text += new_letter
#     print(f"The {user_option}d message is: {final_text}")

# caesar(text_input=message, shift_amount=shift, user_option=options)

# ------------OR-----------------
def caesar(text_input, shift_amount, user_option):
    final_text = ""
    if user_option == "decode":
        shift_amount *= -1
    for letter in text_input:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        final_text += alphabet[new_position]
        print(shift_amount)
    print(f"The {user_option}d message is: {final_text}")

caesar(text_input=message, shift_amount=shift, user_option=options)