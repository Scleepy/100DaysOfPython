from art import logo
import os

def add(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": minus,
    "*": multiply,
    "/": divide,
}

def calc():
    print(logo)

    state = True

    num1 = int(input("What's the first number?: "))

    while state:
        for operation in operations:
            print(operation)

        operation = input("Pick an operation: ")
        
        num2 = int(input("What's the next number?: "))

        result = operations[operation](num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: " ) == "y":
            num1 = result
        else:
            state = False
            os.system("cls")
            calc()

calc()
    



