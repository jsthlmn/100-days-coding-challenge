# from calculator_art import logo

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2): 
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    first_number = int(input("Insert the first number you want to calc: "))

    for i in operations:
        print(i)

    should_continue = True
    while should_continue == True:
        select_operation = input("What operation you want to choose? ")
        second_number = int(input("Insert the next number you want to calc: "))

        calc = operations[select_operation]
        result = calc(first_number, second_number)

        print(f"{first_number} {select_operation} {second_number} is {result}")
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            first_number = result
        else:
            should_continue = False
            calculator()
    
calculator()