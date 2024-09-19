print("Welcome to the Love Calculator!")

your_name = input("What is your name: ").upper()
their_name = input("What is their name: ").upper()

both_names= your_name + their_name

true = both_names.count("T") + both_names.count("R") + both_names.count("U") + both_names.count("E")
love = both_names.count("L") + both_names.count("O") + both_names.count("V") + both_names.count("E")

result = str(true) + str(love)

if int(result) < 10 or int(result) > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif int(result) >= 40 and int(result) <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")

