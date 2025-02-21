from collections import Counter

def main():
    count = Counter(input("Enter a string: "))
    print(sorted(count, key=count.get))

if __name__ == "__main__":
    main()