"""
    Find sum of digits of a given number n
"""

def main():
    n = int(input("Enter a number: "))
    print(f"The sum of digits of {n} = {sum(map(int, str(n * pow(-1, (n < 0)))))}")

if __name__ == "__main__":
    main()