# Aim:
- To explore the use of loops in Python by writing programs for the following and executing them.
m. Print the list of prime numbers between 1 and N.
**Algorithm:**

1. **Input:** Get `N` from the user.
2. **Initialize:** Create an empty list `primes`.
3. **Handle Edge Case:** If `N` is less than 2, print "There are no primes smaller than 2" and stop.
4. **Add 2:** Add 2 to the `primes` list.
5. **Loop through Odd Numbers:** Iterate from 3 to `N` (inclusive), incrementing by 2.
6. **Check for Primality:**
    - Calculate the square root of the current number.
    - Loop through the `primes` list.
    - If the current number is divisible by any prime in the list, it's not prime; break the inner loop.
    - If a prime in the list is greater than the square root of the current number, it means the number is prime. Add it to the `primes` list, and break the inner loop.
7. Print out the list of primes
**Code:**
```py
from math import ceil

def main():
    n = int(input("Enter number upto which you want primes for: "))
    primes = [2]
    if n < 2:
        print("There are no primes smaller than 2")
        return
    
    for i in range(3, n + (n & 1), 2):
        sqrt_i = ceil(i ** .5)
        for prime in primes:
            if not i % prime:
                break
            if prime >= sqrt_i:
                primes.append(i)
                break
    
    print(primes)

if __name__ == "__main__":
    main()
```

**Output:**![[Pasted image 20250324080305.png]]

n. Print the multiplication table up to M for a number N
**Algorithm:**
1. **Input:** Get the number `N` and the upper limit `M` from the user.
2. **Loop:** Iterate from 1 to `M` (inclusive).
3. **Calculate and Print:**
    - Calculate `N * i`.
    - Print `N x i = N * i`.
**Code**:
```py
def main():
    n = int(input("Enter number for which you want multiplication tables: "))
    m = int(input(f"Enter number upto which you want multiplication tables for {n}: "))

    for i in range(1, m + 1):
        print(f"{n} x {i} = {n*i}")

if __name__ == "__main__":
    main()
```

**Output**:![[Pasted image 20250324080510.png]]

o. Print the following pattern for 2N-1 rows.
![[Pasted image 20250324080543.png]]
**Algorithm:**
1. **Input:** Get the number `N` from the user.
2. **Calculate Total Spaces:** Calculate the total number of spaces in the widest row: `2 * N - 1`.
3. **Initialize Lines List:** Create an empty list `lines` to store the rows of the pattern.
4. **Loop for Upper Half:** Iterate from 1 to `N` (inclusive).
    - **Calculate Padding:** Calculate the padding (number of spaces) needed to center the row.
    - **Create Row String:** Create a string with the current number repeated `i` times, separated by spaces.
    - **Right Justify Row:** Right-justify the row string with the calculated padding.
    - **Append to Lines:** Append the justified row to the `lines` list.
    - **Print Row:** Print the row.
5. **Remove Last Row:** Remove the last row from the `lines` list (to avoid duplication).
6. **Loop for Lower Half:** Iterate through the `lines` list in reverse order.
    - **Print Row:** Print each row .
**Code**:
```py
def order(x: int) -> int:
    order = 0
    while x != 0:
        x //= 10
        order += 1

    return order

def main():
    n = int(input("Enter number of rows to print the pattern for: "))
    spaces = 2 * n - 1
    lines = []
    for i in range(1, n + 1):
        padding = int((spaces - (2 * i - 1)) / 2)
        lines.append(" ".join((f"{i}",) * i).rjust(padding + len(f"{i}") * i + i - 1))
        print(lines[-1])
        if i == n:
            lines.pop()
            while lines:
                print(lines.pop())

if __name__ == "__main__":
    main()
```

**Output:**![[Pasted image 20250324080843.png]]

p. Find the greatest common divisor of 2 numbers obtained from the user.
**Algorithm:**
1. **Input:** Get two numbers (`a` and `b`) from the user.
2. **Initialize Sets:** Create two empty sets, `div_a` and `div_b`, to store the divisors of `a` and `b`, respectively.
3. **Find Divisors:**
    - Iterate from 1 to the maximum of `a` and `b` (inclusive).
    - For each number `i`:
        - If `i` is less than `a` and `a` is divisible by `i`, add `i` to `div_a`.
        - If `i` is less than `b` and `b` is divisible by `i`, add `i` to `div_b`.
4. **Find Common Divisors:** Find the intersection of `div_a` and `div_b` (common divisors).
5. **Find Greatest Common Divisor:** Find the maximum value in the intersection set.
6. **Output:** Print the greatest common divisor.
**Code**:
```py
def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    div_a = set()
    div_b = set()

    for i in range(1, max(a, b) + 1):
        if i < a and not a % i:
            div_a.add(i)

        if i < b and not b % i:
            div_b.add(i)

    print(f"Greatest common divisor of {a} and {b} = {max(div_a&div_b)} ")

if __name__ == "__main__":
    main()
```
**Output**:![[Pasted image 20250324081206.png]]

q. Find the sum of the series $1, −(1^2), 2^3, −(3^4), 5^5, −(8^6), 13^7$, … up to N terms.
**Algorithm:**
1. **Input:** Get the number of terms `N` from the user.
2. **Initialize Sum:** Set the `sum` to 1 (the first term).
3. **Handle Edge Case:** If `N` is less than or equal to 0, print 0 and stop.
4. **Loop through Terms:** Iterate from 2 to `N` (inclusive).
5. **Calculate Fibonacci Term:** Calculate the `i`-th Fibonacci number.
6. **Calculate Element:** Calculate the `i`-th element of the series:
    - Raise the `i`-th Fibonacci number to the power of `i`.
    - If `i` is even, multiply the result by -1.
7. **Add to Sum:** Add the calculated element to the `sum`.
8. **Output:** Print the `sum`.
**Code**:
```py
import sys
from functools import cache

sys.set_int_max_str_digits(2500000)


@cache
def fib(n):
    if n <= 0:
        raise ValueError("The nth term implies n be positive, yk?")
    elif n in {1, 2}:
        return 1

    return fib(n - 1) + fib(n - 2)


def main():
    n = int(input("Enter number upto which you want to sum the series: "))
    if n <= 0:
        return print(0)
    sum = 1
    elem = 0
    for i in range(2, n + 1):
        elem = fib(i) ** i
        elem *= -1 if not i & 1 else 1
        sum += elem
    print(sum)


if __name__ == "__main__":
    main()
```

**Output**:![[Pasted image 20250324082653.png]]

r. Find the sum of the digits of a given integer, N.
**Algorithm:**
1. **Input:** Get an integer `N` from the user.
2. **Handle Negative Numbers:**
    - If `N` is negative, make it positive.
3. **Convert to String:** Convert the integer `N` to a string.
4. **Iterate and Sum:**
    - Iterate through each character in the string.
    - Convert each character to an integer.
    - Add the integer to a running sum.
5. **Output:** Print the sum of the digits.
**Code**:
```py
def main():
    n = int(input("Enter a number: "))
    print(f"The sum of digits of {n} = {sum(map(int, str(n * pow(-1, (n < 0)))))}")

if __name__ == "__main__":
    main()
```

**Output**:![[Pasted image 20250324082734.png]]

s. Find the square root of an integer, N, using Newton's method. Obtain N and the
limit, L, from the user.
**Algorithm:**
1. **Input:** Get the integer `N` and the limit (tolerance) `L` from the user.
2. **Handle Negative Input:** If `N` is negative, print an error message (square root of a negative number is not real) and stop.
3. **Initialize Guess:** Set an initial guess for the square root, e.g., `guess = N / 2`.
4. **Iterate and Improve Guess:**
    - Use Newton's method to improve the guess: `new_guess = guess - (guess² - N) / (2 * guess)`.
    - Update `guess` with `new_guess`.
    - Repeat until the difference between `guess²` and `N` is less than the limit `L`.
5. **Output:** Print the final `guess` as the square root of `N`.
**Code**:
```py
from math import isclose

def improve_guess(x: float, n: int) -> float:
    return x - ((x ** 2 - n) / ( 2 * x))

def main():
    n = int(input("Enter integer for which you want to get sqrt for: "))
    if n < 0:
        raise ValueError("Sqrt of negative number does not exist")
    guess = n / 2
    while not isclose(n, guess ** 2, rel_tol=1e-15):
        guess = improve_guess(guess, n)
    print(guess)

if __name__ == "__main__":
    main()
```
**Output**:![[Pasted image 20250324083502.png]]
