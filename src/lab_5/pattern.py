"""
    Print the following pattern for 2n - 1 rows
            1
        2       2
    3       3       3
        2       2
            1
"""

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