"""
    GCD of two numbers
"""

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