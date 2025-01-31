def get_order(n: int) -> int:
    order = 0

    while n !=0:
        n //= 10
        order += 1
    
    return order


def is_armstrong(n: int) -> bool:
    order = get_order(n)
    _n = n
    pow_sum = 0
    for i in range(1, order + 1):
        pow_sum += (_n % 10) ** order
        _n //= 10
    
    return pow_sum == n

def main() -> None:
    n = int(input("Enter number upto which armstrong numbers are to be printed: "))
    print([x for x in range(n + 1) if is_armstrong(x)])

if __name__ == "__main__":
    main()