"""
    Print the list of prime numbers between 1 and N.
"""

from math import ceil

def main():
    n = int(input("Enter number upto which you want primes for: "))
    primes = [2]
    if n < 2:
        print("There are no primes smaller than 2")
        return
    
    for i in range(3, n + (n & 1), 2):
        sqrt_i = ceil(i ** .5)
        for prime in primes:
            if not i % prime:
                break
            if prime >= sqrt_i:
                primes.append(i)
                break
    
    print(primes)

if __name__ == "__main__":
    main()