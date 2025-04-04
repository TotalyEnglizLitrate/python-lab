"""
    Write a function to generate the Collatz sequence starting from a given number n.
    Find no. of steps, maximum value reached and print sequence
"""

def collatz(n):
    if n <= 0:
        print("Input must be a positive integer.")
        return []
    
    sequence = [n]
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence

if __name__ == "__main__":
    while True:
        n = int(input("Enter a positive integer: "))
        result = collatz(n)
        steps = len(result) - 1 if result else 0
        max_value = max(result) if result else None
        print("Collatz sequence:", result)
        print("Number of steps:", steps)
        print("Maximum value reached:", max_value)
        if input("Do you want to continue? (y/n): ").lower() != 'y':
            break