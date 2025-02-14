"""
    Find the roots of a quadratic equation of the form a x^2 + bx + c.
    Get the values of
    a, b, and c from the user and display the roots
"""

import math

def get_user_input():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    return a, b, c

def calculate_roots(a, b, c):
    determinant = b ** 2 - 4 * a * c
    if determinant > 0:
        root1 = (-b + math.sqrt(determinant)) / (2 * a)
        root2 = (-b - math.sqrt(determinant)) / (2 * a)
        print(f"Roots are real and distinct: {root1}, {root2}")
    elif determinant == 0:
        root = -b / (2 * a)
        print(f"Roots are real and equal: {root}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-determinant) / (2 * a)
        print(f"Roots are complex: {complex(real_part, imaginary_part)}")

def main():
    a, b, c = get_user_input()
    calculate_roots(a, b, c)

if __name__ == "__main__":
    main()