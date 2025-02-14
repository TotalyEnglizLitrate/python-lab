"""
    Create a simple calculator that accepts two numbers and an arithmetic operator as
    inputs and performs the appropriate operation on the given numbers and displays
    the result.
"""

def get_input():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %): ")
    num2 = float(input("Enter second number: "))
    return num1, operator, num2

def perform_operation(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed")
            return
    elif operator == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            print("Error: Modulus by zero is not allowed")
            return
    else:
        print("Error: Invalid operator")
        return
    print(f"Result: {result}")

def main():
    while True:
        num1, operator, num2 = get_input()
        perform_operation(num1, operator, num2)
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != "yes":
            return

if __name__ == "__main__":
    main()