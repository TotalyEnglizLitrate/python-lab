"""
    Implement the following using functions from the math module and print the results
    in the scientific notation, approximated to 2 decimal places. Get the values for the
    variables involved from the user:
    (i) Acos(𝜃) - Bsin(𝜃)
    (ii) Acos(2𝜋n)
    (iii) e^an
    (iv) Euclidean distance between two points (x1, x2) and (y1, y2)
    (v) Convert an angle theta from radians to degrees.
    (vi) Find the base 10 and base 2 logarithm of a floating-point number x.
"""

import math

def calculate_expression():
    A = float(input("Enter value of A: "))
    B = float(input("Enter value of B: "))
    theta = float(input("Enter value of theta in radians: "))
    result = A * math.cos(theta) - B * math.sin(theta)
    print(f"A cosθ - B sin(θ) = {result:.2f}")

def calculate_cosine():
    A = float(input("Enter value of A: "))
    n = float(input("Enter value of n: "))
    result = A * math.cos(2 * math.pi * n)
    print(f"A cos(2πn) = {result:.2f}")

def calculate_exponential():
    a = float(input("Enter value of a: "))
    n = float(input("Enter value of n: "))
    result = math.exp(a * n)
    print(f"e^(an) = {result:.2f}")

def calculate_euclidean_distance():
    x1 = float(input("Enter x-coordinate of first point: "))
    x2 = float(input("Enter y-coordinate of first point: "))
    y1 = float(input("Enter x-coordinate of second point: "))
    y2 = float(input("Enter y-coordinate of second point: "))
    result = math.sqrt((x1 - y1) ** 2 + (x2 - y2) ** 2)
    print(f"Euclidean distance = {result:.2f}")

def convert_radians_to_degrees():
    theta = float(input("Enter angle in radians: "))
    result = math.degrees(theta)
    print(f"Angle in degrees = {result:.2f}")

def calculate_logarithm():
    x = float(input("Enter value of x: "))
    result_base10 = math.log10(x)
    result_base2 = math.log2(x)
    print(f"Base 10 logarithm = {result_base10:.2f}")
    print(f"Base 2 logarithm = {result_base2:.2f}")

def main():
    while True:
        print("1. Calculate A cosθ - B sin(θ)")
        print("2. Calculate A cos(2πn)")
        print("3. Calculate e^(an)")
        print("4. Calculate Euclidean distance")
        print("5. Convert radians to degrees")
        print("6. Calculate logarithm")
        print("0. Exit")
        choice = int(input("Enter choice: "))
        if choice == 0:
            break
        elif choice == 1:
            calculate_expression()
        elif choice == 2:
            calculate_cosine()
        elif choice == 3:
            calculate_exponential()
        elif choice == 4:
            calculate_euclidean_distance()
        elif choice == 5:
            convert_radians_to_degrees()
        elif choice == 6:
            calculate_logarithm()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()