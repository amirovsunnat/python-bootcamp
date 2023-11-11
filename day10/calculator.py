import os
from logo import logo


def add(num1, num2):
    """Takes two number and returns added result."""
    return num1 + num2


def subtract(num1, num2):
    """Takes two number and returns result of subtraction."""
    return num1 - num2


def multiply(num1, num2):
    """Takes two number and returns multiplied result."""
    return num1 * num2


def divide(num1, num2):
    """Takes two number and returns divided result."""
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    # asks first number
    number1 = float(input("Enter the first number\n>>> "))
    # shows the operations
    for operator in operations:
        print(operator)
    wants_calculate = True
    while wants_calculate:
        # asks operation
        operator = input("Choose the operator\n>>> ")
        # asks second number
        number2 = float(input("Enter the next number\n>>> "))
        # find the operation
        operation = operations[operator]
        # calculates the result
        answer = operation(number1, number2)
        # print the end result
        print(f"{number1} {operator} {number2} = {answer}")
        want_to_calculate_again = input(f"Do you want to continue calculating"
                                        f" with the value of {answer}?"
                                        f"If you want to start new calculator type (n|new)\n>>> ").strip().lower()
        if want_to_calculate_again == "yes":
            number1 = answer
        else:
            want_to_calculate_again = False
            os.system("cls")
            calculator()


calculator()
