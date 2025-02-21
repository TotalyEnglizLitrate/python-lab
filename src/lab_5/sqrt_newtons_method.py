"""
    Find the square root of an integer using newtons method
"""

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