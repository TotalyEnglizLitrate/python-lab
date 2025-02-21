def alternate_concat(s1, s2):
    result = []
    for c1, c2 in zip(s1, s2):
        result.append(c1) if c1 else ...
        result.append(c2) if c2 else ...
    return ''.join(result)

def main():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    if len(s1) != len(s2):
        print("Both strings must be of the same length.")
    else:
        result = alternate_concat(s1, s2)
        print("Resultant string:", result)

if __name__ == "__main__":
    main()
