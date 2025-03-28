# Aim:
- To explore the use of conditional statements in Python by writing programs for the following and executing them

g. Create a simple calculator that accepts two numbers and an arithmetic operator as inputs and performs the appropriate operation on the given numbers and displays
the result.

**Algorithm:**
1. **Input:** Get two numbers (`num1`, `num2`) and an operator (`operator`) from the user.
2. **Conditional:**
    - If `operator` is "+", calculate `result = num1 + num2`.
    - If `operator` is "-", calculate `result = num1 - num2`.
    - If `operator` is "*", calculate `result = num1 * num2`.
    - If `operator` is "/":
        - If `num2` is not 0, calculate `result = num1 / num2`.
        - Else, print "Error: Division by zero is not allowed" and stop.
    - If `operator` is "%":
        - If `num2` is not 0, calculate `result = num1 % num2`.
        - Else, print "Error: Modulus by zero is not allowed" and stop.
    - Else, print "Error: Invalid operator" and stop.
3. **Output:** Print the `result`.
4. **Loop:**
    - Ask if the user wants to continue.
    - If yes, repeat from step 1.
    - Else, stop.**Algorithm:**

5. **Input:** Get two numbers (`num1`, `num2`) and an operator (`operator`) from the user.
6. **Conditional:**
    - If `operator` is "+", calculate `result = num1 + num2`.
    - If `operator` is "-", calculate `result = num1 - num2`.
    - If `operator` is "*", calculate `result = num1 * num2`.
    - If `operator` is "/":
        - If `num2` is not 0, calculate `result = num1 / num2`.
        - Else, print "Error: Division by zero is not allowed" and stop.
    - If `operator` is "%":
        - If `num2` is not 0, calculate `result = num1 % num2`.
        - Else, print "Error: Modulus by zero is not allowed" and stop.
    - Else, print "Error: Invalid operator" and stop.
7. **Output:** Print the `result`.
8. **Loop:**
    - Ask if the user wants to continue.
    - If yes, repeat from step 1.
    - Else, stop.

**Code:**
```py
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
```
**Output**:![[Pasted image 20250324023647.png]]
h. Get a year from the user and check if it is a leap year and display the result
**Algorithm:**
1. **Input:** Get a year from the user.
2. **Check Leap Year:**
    - If the year is divisible by 400, it's a leap year.
    - Else, if the year is divisible by 100, it's not a leap year.
    - Else, if the year is divisible by 4, it's a leap year.
    - Else, it's not a leap year.
3. **Output:** Display whether the year is a leap year or not.
**Code**:
```
def check_leap_year(year):
    chk = tuple(map(lambda x: not (year % x), (4, 100, 400)))
    if chk[2]:
        return True
    elif chk[1]:
        return False
    elif chk[0]:
        return True

    return False


def main():
    year = int(input("Enter a year: "))
    print(f"{year} is{' ' if check_leap_year(year) else ' not '} a leap year")


if __name__ == "__main__":
    main()
```
**Output**:![[Pasted image 20250324024914.png]]
i. Find the maximum of three numbers, obtained from the user, using conditional
statements
**Algorithm:**
1.  **Input:** Get three numbers (`num1`, `num2`, `num3`) from the user.
2.  **Conditional:**
    * If `num1` is greater than or equal to `num2` and `num1` is greater than or equal to `num3`, print `num1` as the maximum.
    * Else if `num2` is greater than or equal to `num1` and `num2` is greater than or equal to `num3`, print `num2` as the maximum.
    * Else, print `num3` as the maximum.
3.  **Output:** Print the maximum number.
**Code**:
```py
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
```
**Output**:![[Pasted image 20250324025103.png]]
j. Obtain the marks secured by a student in Maths, Physics, Chemistry, Computer Science, and English, out of 100, and calculate their average. Check the range within which the average mark falls and display the appropriate grade. (A+ grade - 90 to 100, A grade - 80 to 90, B+ grade - 70 to 80, B grade - 60 to 70, C grade - 50 to 60, D grade - 40 to 50, F grade - less than 40)
**Algorithm:**
1. **Input:** Get marks for Maths, Physics, Chemistry, Computer Science, and English from the user.
2. **Calculate Average:** Compute the average of the marks.
3. **Check Grade:**
    - If average is between 90 and 100, print "Average mark: [average], Grade: A+".
    - Else if average is between 80 and 90, print "Average mark: [average], Grade: A".
    - Else if average is between 70 and 80, print "Average mark: [average], Grade: B+".
    - Else if average is between 60 and 70, print "Average mark: [average], Grade: B".
    - Else if average is between 50 and 60, print "Average mark: [average], Grade: C".
    - Else if average is between 40 and 50, print "Average mark: [average], Grade: D".
    - Else, print "Average mark: [average], Grade: F".
**Code**:
```py
def get_user_input():
    maths = float(input("Enter marks in Maths: "))
    physics = float(input("Enter marks in Physics: "))
    chemistry = float(input("Enter marks in Chemistry: "))
    computer_science = float(input("Enter marks in Computer Science: "))
    english = float(input("Enter marks in English: "))
    return maths, physics, chemistry, computer_science, english

def check_grade(average):
    if average >= 90 and average <= 100:
        print(f"Average mark: {average:.2f}, Grade: A+")
    elif average >= 80 and average < 90:
        print(f"Average mark: {average:.2f}, Grade: A")
    elif average >= 70 and average < 80:
        print(f"Average mark: {average:.2f}, Grade: B+")
    elif average >= 60 and average < 70:
        print(f"Average mark: {average:.2f}, Grade: B")
    elif average >= 50 and average < 60:
        print(f"Average mark: {average:.2f}, Grade: C")
    elif average >= 40 and average < 50:
        print(f"Average mark: {average:.2f}, Grade: D")
    else:
        print(f"Average mark: {average:.2f}, Grade: F")

def main():
    maths, physics, chemistry, computer_science, english = marks = get_user_input()
    average = sum(marks) / len(marks)
    check_grade(average)

if __name__ == "__main__":
    main()
```
**Output**:![[Pasted image 20250324025340.png]]
k. identify if a point (x,y) lies inside, outside, or on the circumference of a circle of
radius "r", centered at the origin. Obtain the values of x, y, and r from the user.
**Algorithm:**
1. **Input:** Get the x-coordinate (`x`), y-coordinate (`y`), and radius (`r`) from the user.
2. **Calculate Distance:** Compute the distance of the point (x, y) from the origin using the formula `distance = sqrt(x² + y²)`.
3. **Conditional:**
    - If `distance < r`, print "The point (x, y) lies inside the circle of radius r."
    - Else if `distance > r`, print "The point (x, y) lies outside the circle of radius r."
    - Else, print "The point (x, y) lies on the circumference of the circle of radius r."
**Code**:
```py
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
```
**Output**:![[Pasted image 20250324025531.png]]
l. Obtain the lengths of the 4 sides of a quadrilateral and the angles at each corner of
the quadrilateral. Verify if the dimensions represent a valid quadrilateral and if so,
check whether the dimensions represent a square, a rectangle, or neither
**Algorithm:**
1. **Input:** Get the lengths of the four sides and the angles at each corner of the quadrilateral from the user.
2. **Check Valid Quadrilateral:**
    - Check if the sum of the angles is 360 degrees.
    - Check if the sum of any three sides is greater than the fourth side (triangle inequality).
    - If both conditions are true, the quadrilateral is valid; otherwise, it's invalid.
3. **Check Square:**
    - If all sides are equal and all angles are 90 degrees, the quadrilateral is a square.
4. **Check Rectangle:**
    - If opposite sides are equal and all angles are 90 degrees, the quadrilateral is a rectangle.
5. **Output:**
    - If the quadrilateral is invalid, print "The dimensions do not represent a valid quadrilateral."
    - If it's a square, print "The dimensions represent a square."
    - If it's a rectangle, print "The dimensions represent a rectangle."
    - Otherwise, print "The dimensions represent neither a square nor a rectangle."**
**Code:**
```py
from itertools import combinations


def get_user_input():
    sides = tuple(float(input(f"Enter length of side {i+1}: ")) for i in range(4))
    angles = tuple(float(input(f"Enter angle at corner {i+1} (in degrees): ")) for i in range(4))
    return sides, angles


def check_valid_quadrilateral(sides, angles):
    if sum(angles) == 360:
        ineq = lambda x: x[0] + x[1] >= x[2]
        if all(map(ineq, combinations(sides, 3))):
            return True
        else:
            print("The dimensions do not represent a valid quadrilateral.")
            return False
    else:
        print("The dimensions do not represent a valid quadrilateral.")
        return False


def check_square(sides, angles):
    if sides[0] == sides[1] == sides[2] == sides[3] and angles[0] == angles[1] == angles[2] == angles[3] == 90:
        return True
    else:
        return False


def check_rectangle(sides, angles):
    if (sides[0] == sides[2] and sides[1] == sides[3]) or (sides[0] == sides[1] and sides[2] == sides[3]):
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
```
**Output**:![[Pasted image 20250324032859.png]]

# Result
- Thus, programs have been written and executed to explore the use of conditional
statements in Python.