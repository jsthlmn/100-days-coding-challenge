MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough water")

current_money = 0

machine_off = False
while not machine_off :
    # Ask the user for the options
    # TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: 2. Turn off the coffe machine by entering "off" to the prompt.
    if user_input == "off":
        machine_off = True
    elif user_input == "report":
        # TODO: 3. Print report
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {current_money}")
    else:
        drink = MENU[user_input]
        is_resource_sufficient(drink["ingredients"])


# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.
