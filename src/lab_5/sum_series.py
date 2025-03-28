"""
    Find the sum of the series 1, -(1 ** 2), 2 ** 3, -(3 ** 4)..... upto n terms
"""

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
