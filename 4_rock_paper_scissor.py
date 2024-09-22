import random

print("Welcome to Rock, Paper, Scissors Game!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissor]

user_choice = input("What do you choose, Type 0 for Rock, 1 for Paper, or 2 for Scissor: ")
int_user_choice = int(user_choice)
computer_choice = random.randint(0, 2)

if int_user_choice < 0 or int_user_choice >=3:
    print("Enter the number between 0 and 2")
elif int_user_choice >=0 and int_user_choice <3:
    print(f"Your choose {game_images[int_user_choice]} \nThe computer choose {game_images[computer_choice]}")

    if int_user_choice == computer_choice:
        print("It's a tie")
    elif int_user_choice == 0 and computer_choice == 1:
        print("You lose")
    elif int_user_choice == 0 and computer_choice == 2:
        print("You win")
    elif int_user_choice == 1 and computer_choice == 0:
        print("You win")
    elif int_user_choice == 1 and computer_choice == 2:
        print("You lose")
    elif int_user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif int_user_choice == 2 and computer_choice == 1:
        print("You win")