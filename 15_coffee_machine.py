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
current_money = 0


# TODO: 4. Check resources sufficient?
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, and False if ingredients are insufficient."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough


# TODO: 5. Process coins
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# TODO: 6. Check transaction successful?
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is successful, of False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global current_money
        current_money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 7. Make Coffee.
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")


machine_off = False
while not machine_off:
    # Ask the user for the options
    # TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: 2. Turn off the coffe machine by entering "off" to the prompt.
    if user_input == "off":
        machine_off = True
    elif user_input == "report":
        # TODO: 3. Print report
        print(
            f"Water: {resources['water']}ml"
            f"\nMilk: {resources['milk']}ml"
            f"\nCoffee: {resources['coffee']}g"
            f"\nMoney: {current_money}"
        )
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])