import random

your_choice = input("Choose Heads or Tails: ").lower()
computer_choice = random.choice(["heads", "tails"])

print(f"You chose {your_choice} and the computer chose {computer_choice}")

if your_choice == "heads" or your_choice == "tails":
    if your_choice == computer_choice:
        print("Your'e right")
    elif your_choice != computer_choice:
        print("Better luck next time")
else:
    print("You enter an invalid choice")