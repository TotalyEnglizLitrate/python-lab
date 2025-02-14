"""
    Find the maximum of three numbers, obtained from the user, using conditional statements.
"""


def find_max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(f"Maximum number is: {num1}")
    elif num2 >= num1 and num2 >= num3:
        print(f"Maximum number is: {num2}")
    else:
        print(f"Maximum number is: {num3}")

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    find_max(num1, num2, num3)

if __name__ == "__main__":
    main()