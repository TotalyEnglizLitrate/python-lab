import numpy as np

from math import isclose
from numpy.polynomial import Polynomial

def eval_func(func: Polynomial, point: np.float128):
    return sum(np.float128(point ** idx * i) for idx, i in enumerate(func.coef))

def improve_guess(func: Polynomial, guess: np.float128):
    adjust = (eval_func(func, guess) / eval_func(func.deriv(), guess))
    return guess - adjust

def find_root(func: Polynomial, lower_bound: np.float128, upper_bound: np.float128):
    if lower_bound > upper_bound:
        print("Lower bound must be lesser than Upper bound")
    guess = (lower_bound + upper_bound) / np.float128(2)
    a_val = eval_func(func, lower_bound)
    b_val = eval_func(func, upper_bound)
    print(a_val, b_val)
    if a_val < 0 and b_val < 0 or a_val > 0 and b_val > 0:
        print("lower and upper bound function values have the same sign")

    while not isclose(eval_func(func, guess), .0, rel_tol=1e-12):
        new_guess = improve_guess(func, guess)
        if guess == new_guess:
            break
        guess = new_guess
        print(guess, eval_func(func, guess))

    return guess

coeffs = []
i = 0
while True:
    coeffs.append(np.float128(input(f"Enter coeff {i}: ")))
    i += 1
    if input("Continue?").lower() == "n":
        break

print(find_root(Polynomial(coeffs), np.float128(-1), np.float128(0)))