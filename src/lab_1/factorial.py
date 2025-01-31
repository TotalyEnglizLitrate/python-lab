def fact(n: int) -> int:
    if n < 0:
        raise ValueError("Cannot calculate factorial of a negative number")
    
    prod = 1
    for x in range(1, n + 1):
        prod *= x
    
    return prod


def fact_recur(n: int) -> int:
    if n < 0:
        raise ValueError("Cannot calculate factorial of a negative number")
    
    if n in {0, 1}:
        return 1
    
    return fact_recur(n - 1) * n


def main() -> None:
    n = int(input("Enter number whose factorial is to be calculated: "))
    print(f"Recursion: {fact_recur(n)}")
    print(f"Loop: {fact(n)}")


if __name__ == "__main__":
    main()