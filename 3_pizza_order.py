print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want to add pepperoni? Y or N ")
extra_cheese = input("Do you want to add an extra cheese? Y or N ")

small_pizaa = 15
medium_pizza = 20
large_pizza = 25

pepperoni_small = 2
pepperoni_med_large = 3

extra_cheese = 1

bill = 0

if size == "S":
    bill = small_pizaa
    if add_pepperoni == "Y":
        bill += pepperoni_small
    print(f"Your final bill is ${bill}.")
elif size == "M":
    bill = medium_pizza
    if add_pepperoni == "Y":
        bill += pepperoni_med_large
    print(f"Your final bill is ${bill}.")
elif size == "L":
    bill = large_pizza
    if add_pepperoni == "Y":
        bill += pepperoni_med_large
    print(f"Your final bill is ${bill}.")
else:
    print("Your final bill is $0.")