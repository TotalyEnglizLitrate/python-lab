"""
Obtain the lengths of the 4 sides of a quadrilateral and the angles at each corner of the quadrilateral. Verify if the dimensions represent a valid quadrilateral and if so, check whether the dimensions represent a square, a rectangle, or neither.
"""

from itertools import combinations

def get_user_input():
    sides = tuple(float(input(f"Enter length of side {i+1}: ")) for i in range(4))
    angles = tuple(float(input(f"Enter angle at corner {i+1} (in degrees): ")) for i in range(4))
    return sides, angles

def check_valid_quadrilateral(sides, angles):
    if sum(angles) == 360:
        ineq = lambda x, y, z: x + y > z
        if all(map(ineq, combinations(sides, 3))):
            return True
        else:
            print("The dimensions do not represent a valid quadrilateral.")
            return False
    else:
        print("The dimensions do not represent a valid quadrilateral.")
        return False

def check_square(sides, angles):
    if (sides[0] == sides[1] == sides[2] == sides[3]
        and
        angles[0] == angles[1] == angles[2] == angles[3] == 90):
        return True
    else:
        return False

def check_rectangle(sides, angles):
    if ((sides[0] == sides[2] and sides[1] == sides[3])
        or
        (sides[0] == sides[1] and sides[2] == sides[3])):
        if angles[0] == angles[2] == 90 and angles[1] == angles[3] == 90:
            return True
        else:
            return False
    else:
        return False

def main():
    sides, angles = get_user_input()
    if check_valid_quadrilateral(sides, angles):
        if check_square(sides, angles):
            print("The dimensions represent a square.")
        elif check_rectangle(sides, angles):
            print("The dimensions represent a rectangle.")
        else:
            print("The dimensions represent neither a square nor a rectangle.")

if __name__ == "__main__":
    main()