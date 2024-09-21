print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type 'left or right': ").lower()

if direction == "left":
    lake = input("You cam to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if lake == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if door == "yellow":
            print("You Win!")
        elif door == "red":
            print("You enter a room of beasts. Game Over!")
        elif door == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("The you chose in not in the option. Game Over")
    elif lake == "swim":
        print("There is a shark in the water. Game Over")
    else:
        print("The direction you chose in not in the option. Game Over")
else:
    print("You chose the wrong direction. Game Over")