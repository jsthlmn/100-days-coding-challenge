print("Welcome to the bill calculator!")

total_bill = input("What was the total bill? ")
tax = 12
tip = input("How much of tip you want to add? ")
people = input("How many people to split the bill? ")

total_pay = (float(total_bill) + (int(tax) / 100) * float(total_bill)) + int(tip)

result = round(total_pay / int(people), 2) 

print(f"The all total you have to pay after tax 12% ${total_pay}, so each person should pay ${result}")