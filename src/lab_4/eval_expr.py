"""
    Write a program (script mode) to get two integers from a user, store them in variables
    a and a, and evaluate the following expression:
    c = ((a+b)^2 + 10)/(a*b)
"""

def main():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print(f"The expression c = {(((a + b) ** 2 + 10)/(a * b))=}")

if __name__ == "__main__":
    main()