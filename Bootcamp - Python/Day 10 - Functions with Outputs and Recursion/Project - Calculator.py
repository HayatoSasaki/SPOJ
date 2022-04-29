from replit import clear
from art import logo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator(n1):
    op = input("Which operation do you want to do? + - * /\n")
    n2 = int(input("What's is the second number? "))

    result = operations[op](n1, n2)
    print(f"{n1} {op} {n2} = {result}")

    again = input(f"Type 'y' to continue calculating with {result}.")
    if again == 'y':
        clear()
        calculator(result)
    else:
        return

calculator(int(input("What's is the first number? ")))