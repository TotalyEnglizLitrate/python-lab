"""
    Identify if a point (x,y) lies inside, outside, or on the circumference of a circle of radius "r",
    centered at the origin. Obtain the values of x, y, and r from the user.
"""

import math

def check_point(x, y, r):
    distance = math.sqrt(x ** 2 + y ** 2)
    if distance < r:
        print(f"The point ({x}, {y}) lies inside the circle of radius {r}.")
    elif distance > r:
        print(f"The point ({x}, {y}) lies outside the circle of radius {r}.")
    else:
        print(f"The point ({x}, {y}) lies on the circumference of the circle of radius {r}.")

def main():
    x = float(input("Enter x-coordinate of the point: "))
    y = float(input("Enter y-coordinate of the point: "))
    r = float(input("Enter radius of the circle: "))
    check_point(x, y, r)

if __name__ == "__main__":
    main()