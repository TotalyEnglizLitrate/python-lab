def fib(n: int) -> list[int]:
    terms = [1, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    
    for i in range(2,n):
        terms.append(terms[i-1] + terms[i-2])
    
    return terms


def main() -> None:
    n = int(input("Enter number of terms upto which fibonacci sequence is to be calculated: "))
    print(fib(n))


if __name__ == "__main__":
    main()