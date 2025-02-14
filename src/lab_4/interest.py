"""
    Calculate the simple interest and compound interest, given the principal amount (P),
    rate of interest (R), term of deposit (T) (in years), and number of times interest is
    compounded in a year (n) from the user. Display the result rounded off to 4 decimal
    places.
"""

def compound_interest(principal: float, rate: float, time: float, n: int = 1):
    assert n > 0, "Number of times interest is compunded must be positive"
    return (principal * rate / (n * 100)) ** (n * time)

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