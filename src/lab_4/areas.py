"""
    Get the dimensions (floating point values) of a triangle, parallelogram, cylinder,
    cone, sphere, and rectangular prism, calculate each of their areas and display the
    result as a floating-point number approximated to 2 decimal places.
"""

import math


def ar_trngl(base: float, height: float) -> float:
    return ar_parallelogram(base, height) / 2

def ar_parallelogram(base: float, height: float) -> float:
    return base * height

def total_ar_cone(base_r: float, height: float) -> float:
    slant = math.sqrt(base_r ** 2 + height ** 2)
    return math.pi * base_r  * (base_r + slant)

def ar_sphere(radius: float) -> float:
    return 4 * math.pi * radius ** 2

def ar_rect_prism(length: float, breadth: float, height: float) -> float:
    return 2 * (length * height + length * breadth + breadth * height)

def menu():
    print(
    "1. Triangle",
    "2. Parallelogram",
    "3. Cone",
    "4. Sphere",
    "5. Cuboid",
    "0. Exit"
    )
    choice = int(input("Enter choice: "))

    if choice == 0:
        exit(0)
    elif choice == 1:
        base = float(input("Enter base of triangle: "))
        height = float(input("Enter height of triangle: "))
        print(f"The area of the given triangle is: {ar_trngl(base, height):.2f}")
    elif choice == 2:
        base = float(input("Enter base of parallelogram: "))
        height = float(input("Enter height of parallelogram: "))
        print(f"The area of the given parallelogram is: {ar_parallelogram(base, height):.2f}")
    elif choice == 3:
        base_r = float(input("Enter base radius of cone: "))
        height = float(input("Enter height of cone: "))
        print(f"The total surface area of the given cone is {total_ar_cone(base_r, height):.2f}")
    elif choice == 4:
        radius = float(input("Enter radius of the sphere: "))
        print(f"The total surface area of the given sphere is {ar_sphere(radius):.2f}")
    elif choice == 5:
        length = float(input("Enter length of the cuboid: "))
        breadth = float(input("Enter breadth of the cuboid: "))
        height = float(input("Enter height of the cuboid: "))
        print(f"The total surface area of the given cuboid is: {ar_rect_prism(length, breadth, height):.2f}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    while True:
        menu()