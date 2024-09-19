print("Welcom to the rollercoaster!")

height = int(input("What is your height in cm? "))
photos_fee = 3
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Kids under 12 bill is $5.")
    elif age <= 18:
        bill = 7
        print("Teenagers bill is $7.")
    elif age > 18 and age < 45:
        bill = 12
        print("Age over 18 the bill is $12.")
    elif age >= 45 and age <= 55:
        print("You got a free ticket.")
    else:
        print("You are too old to ride.")

    photos = input("Do you want photos taken? (Yes or No) ")
    if photos == "Yes":
        bill += photos_fee
    
    print(f"Your total bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")