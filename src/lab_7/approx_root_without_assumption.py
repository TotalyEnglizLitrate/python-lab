import numpy as np

from math import isclose
from numpy.polynomial import Polynomial

def eval_func(func: Polynomial, point: np.float128):
    return sum(np.float128(point ** idx * i) for idx, i in enumerate(func.coef))

def improve_guess(func: Polynomial, guess: np.float128):
    adjust = (eval_func(func, guess) / eval_func(func.deriv(), guess))
    return guess - adjust

def find_root(func: Polynomial):
    guess = 0
    
    while not isclose(eval_func(func, guess), .0, rel_tol=1e-30):
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

print(find_root(Polynomial(coeffs)))