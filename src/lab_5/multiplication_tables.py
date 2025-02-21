"""
    Print the multiplication tables upto M for a number N
"""

def main():
    n = int(input("Enter number for which you want multiplication tables: "))
    m = int(input(f"Enter number upto which you want multiplication tables for {n}: "))

    for i in range(1, m + 1):
        print(f"{n} x {i} = {n*i}")

if __name__ == "__main__":
    main()