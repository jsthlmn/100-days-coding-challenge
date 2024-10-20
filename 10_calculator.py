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

first_number = int(input("Insert the first number you want to calc: "))

for i in operations:
    print(i)
select_operation = input("What operation you want to choose?")
second_number = int(input("Insert the second number you want to calc: "))

calc = operations[select_operation]
result = calc(first_number, second_number)

print(f"{first_number} {select_operation} {second_number} is {result}")
    