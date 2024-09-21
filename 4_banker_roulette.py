import random

name_string = input("Give me everybody's names, separated by a comma: ")

# names = name_string.split(", ")
# people_to_pay = random.choice(names)

# print(f"{people_to_pay} is going to buy the meal today!")

# --------Atau---------

names = name_string.split(", ")
num_items = len(names)

random_choice = random.randint(0, num_items -1)
people_who_pay = names[random_choice]

print(f"{people_who_pay} is going to buy the meal today!")