# Aim:
- To explore the use of operators and expressions in Python by writing programs for the
following and executing them.

a. Get the dimensions (floating point values) of a triangle, parallelogram, cylinder, cone, sphere, and rectangular prism, calculate each of their areas and display the result as a floating-point number approximated to 2 decimal places.
**Algorithm**:
- Step 1: Menu to pick shape for which area is to be calculated
- Step 2: Get the required dimensions to calculate the respective shape's area
- Step 3: Calculate it's area, rounded to 2 decimal places and print it out
**Code**:
```py
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
```
**Output**:![[Pasted image 20250324012305.png]]
b. Calculate the simple interest and compound interest, given the principal amount (P),
rate of interest (R), term of deposit (T) (in years), and number of times interest is
compounded in a year (n) from the user. Display the result rounded off to 4 decimal
places.

**Algorithm**:
- Step 1: Take in principal amount, rate of interest, time, and number times interest is compounded per year.
- Step 2: Calculate simple and compound interest and print it out, rounded to 4 decimal places
**Code**:
```py
def compound_interest(principal: float, rate: float, time: float, n: int = 1):
    assert n > 0, "Number of times interest is compunded must be positive"
    return principal * (1 + rate / (n * 100)) ** (n * time) - principal

def simple_interest(principal: float, rate: float, time: float):
    return principal * rate * time / 100

def main():
    p = float(input("Enter principal: "))
    r = float(input("Enter rate: "))
    t = float(input("Enter time: "))
    n = int(input("Enter number of times interest is compounded in a year: "))

    print(f"Simple interest: {simple_interest(p, r, t):.4f}")
    print(f"Compound interest: {compound_interest(p, r, t, n):.4f}")

if __name__ == "__main__":
    main()
```
**Output**:![[Pasted image 20250324014314.png]]
c. Calculate the salary of an employee of a company in terms of the basic pay, dearness allowance (DA), and house rent allowance (HRA). The DA and HRA are set as a certain percentage of the basic pay. Further, the company deducts 12% of the basic pay for PF. Compute the salary that would be received by an employee given the basic pay, percentage of basic pay for DA, and percentage of basic pay for HRA and print it, rounded off to the nearest integer. (Salary = Basic Pay + DA + HRA - PF)
**Algorithm**:
- Step 1: Get the basic pay, dearness allowance (DA) percentage, and house rent allowance (HRA) percentage as input from the user.
- Step 2: Calculate the DA amount by multiplying the basic pay by the DA percentage divided by 100.
- Step 3: Calculate the HRA amount by multiplying the basic pay by the HRA percentage divide by 100.
- Step 4: Calculate the Provident Fund (PF) deduction, which is 12% of the basic pay.
- Step 5: Calculate the total salary by adding the basic pay, DA, and HRA, and then subtracting the PF deduction.
- Step 6: Round the calculated salary to the nearest integer.
- Step 7: Print the rounded salary.
**Code**:
```py
def calculate_salary(basic_pay, da_percentage, hra_percentage):
    da = (da_percentage / 100) * basic_pay
    hra = (hra_percentage / 100) * basic_pay
    pf = 0.12 * basic_pay
    salary = basic_pay + da + hra - pf
    return round(salary)

def main():
    basic_pay = float(input("Enter basic pay: "))
    da_percentage = float(input("Enter percentage of basic pay for DA: "))
    hra_percentage = float(input("Enter percentage of basic pay for HRA: "))
    salary = calculate_salary(basic_pay, da_percentage, hra_percentage)
    print(f"The salary of the employee is: {salary}")

if __name__ == "__main__":
    main()
```

**Output**:![[Pasted image 20250324015226.png]]
d. Implement the following using functions from the math module and print the results
in the scientific notation, approximated to 2 decimal places. Get the values for the
variables involved from the user:
(i) 𝐴 𝑐𝑜𝑠𝜃 − 𝐵 𝑠𝑖𝑛(𝜃)
(ii) 𝐴 𝑐𝑜𝑠(2𝜋𝑛)
(iii) $𝑒^{𝑎𝑛}$
(iv) Euclidean distance between two points $(x_{1}, x_{2}) \text{ and } (y_{1}, y_{2})$ (Use the formula for Euclidean distance - √$(𝑥_{1} − 𝑥_{2})^2 + (𝑦_{1} − 𝑦_{2})^2)$
(v) Convert an angle theta from radians to degrees.
(vi) Find the base 10 and base 2 logarithm of a floating-point number x.
**Algorithm 1:**

1. **Input:** Get `A`, `B`, and `theta` (radians).
2. **Calculate:** Compute `A * cos(theta) - B * sin(theta)`.
3. **Output:** Print the result in scientific notation (2 decimal places).

**Algorithm 2:**

1. **Input:** Get `A` and `n`.
2. **Calculate:** Compute `A * cos(2 * pi * n)`.
3. **Output:** Print the result in scientific notation (2 decimal places).

**Algorithm 3:**

1. **Input:** Get `a` and `n`.
2. **Calculate:** Compute `e^(a * n)`.
3. **Output:** Print the result in scientific notation (2 decimal places).

**Algorithm 4:**

1. **Input:** Get `x1`, `x2`, `y1`, `y2`.
2. **Calculate:** Compute `sqrt((x1 - y1)^2 + (x2 - y2)^2)`.
3. **Output:** Print the result in scientific notation (2 decimal places).

**Algorithm 5:**

1. **Input:** Get `theta` (radians).
2. **Calculate:** Convert `theta` to degrees.
3. **Output:** Print the result (2 decimal places).

**Algorithm 6:**

1. **Input:** Get `x`.
2. **Calculate:** Compute `log10(x)` and `log2(x)`.
3. **Output:** Print both results in scientific notation (2 decimal places).

**Algorithm 7:**

1. **Loop:** Repeat until user chooses to exit.
2. **Menu:** Display options for calculations.
3. **Input:** Get user's choice.
4. **Conditional:**
    - If choice is 1, call function for `A cosθ - B sin(θ)`.
    - If choice is 2, call function for `A cos(2πn)`.
    - If choice is 3, call function for `e^(an)`.
    - If choice is 4, call function for Euclidean distance.
    - If choice is 5, call function for radians to degrees.
    - If choice is 6, call function for logarithms.
    - If choice is 0, exit.
    - Else, display "Invalid choice".
**Code**:
```py
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
```

**Output**:![[Pasted image 20250324020217.png]]
e. Obtain 2 decimal numbers from the user, display them in binary, octal, and hexadecimal forms, perform the logical operations (and, or, not, left and right shift) and print the results in binary and decimal forms.

**Algorithm:**
- Step 1: **Input:** Get two decimal numbers from the user.
- Step 2: **Display Base Forms:**
    - Convert each number to binary, octal, and hexadecimal forms.
    - Print the results.
- Step 3: **Perform Logical Operations:**
    - Calculate the bitwise AND of the two numbers.
    - Calculate the bitwise OR of the two numbers.
    - Calculate the bitwise NOT of each number.
    - Calculate the left shift of each number by 1 bit.
    - Calculate the right shift of each number by 1 bit.
- Step 4: **Output Results:**
    - Print the results of each logical operation in binary and decimal forms.
**Code:**
```py
def get_user_input():
    num1 = int(input("Enter first decimal number: "))
    num2 = int(input("Enter second decimal number: "))
    return num1, num2

def display_base_forms(num1, num2):
    print(f"Binary form of {num1}: {bin(num1)}")
    print(f"Octal form of {num1}: {oct(num1)}")
    print(f"Hexadecimal form of {num1}: {hex(num1)}")
    print(f"Binary form of {num2}: {bin(num2)}")
    print(f"Octal form of {num2}: {oct(num2)}")
    print(f"Hexadecimal form of {num2}: {hex(num2)}")

def perform_logical_operations(num1, num2):
    and_result = num1 & num2
    or_result = num1 | num2
    not_result1 = ~num1
    not_result2 = ~num2
    left_shift_result1 = num1 << 1
    left_shift_result2 = num2 << 1
    right_shift_result1 = num1 >> 1
    right_shift_result2 = num2 >> 1
    print(f"And operation: {bin(and_result)} ({and_result})")
    print(f"Or operation: {bin(or_result)} ({or_result})")
    print(f"Not operation on {num1}: {bin(not_result1)} ({not_result1})")
    print(f"Not operation on {num2}: {bin(not_result2)} ({not_result2})")
    print(f"Left shift operation on {num1}: {bin(left_shift_result1)} ({left_shift_result1})")
    print(f"Left shift operation on {num2}: {bin(left_shift_result2)} ({left_shift_result2})")
    print(f"Right shift operation on {num1}: {bin(right_shift_result1)} ({right_shift_result1})")
    print(f"Right shift operation on {num2}: {bin(right_shift_result2)} ({right_shift_result2})")

def main():
    num1, num2 = get_user_input()
    display_base_forms(num1, num2)
    perform_logical_operations(num1, num2)

if __name__ == "__main__":
    main()
```
**Output**:![[Pasted image 20250324020852.png]]
f. Find the roots of a quadratic equation of the form 𝑎𝑥2 + 𝑏𝑥 + 𝑐. Get the values of a, b, and c from the user and display the roots.
**Algorithm:**
1. **Input:** Get values for `a`, `b`, and `c` from the user.
2. **Calculate Determinant:** Compute `determinant = b² - 4ac`.
3. **Conditional:**
    - If `determinant > 0`:
        - Calculate `root1 = (-b + sqrt(determinant)) / (2a)`.
        - Calculate `root2 = (-b - sqrt(determinant)) / (2a)`.
        - Print "Roots are real and distinct: `root1`, `root2`".
    - Else if `determinant == 0`:
        - Calculate `root = -b / (2a)`.
        - Print "Roots are real and equal: `root`".
    - Else:
        - Calculate `real_part = -b / (2a)`.
        - Calculate `imaginary_part = sqrt(-determinant) / (2a)`.
        - Print "Roots are complex: `complex(real_part, imaginary_part)`".
**Code:**
```py
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
```
**Output:**![[Pasted image 20250324022451.png]]

# Result
-  Thus, programs have been written and executed to explore the use of operators and
expressions in Python