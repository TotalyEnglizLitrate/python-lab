def count_substrings(s):
    count = 0
    for length in range(1, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i : i + length]
            if substring[0] == substring[-1] and len(substring) > 1:
                count += 1
    return count


def main():
    s = input("Enter string to test: ")
    count = count_substrings(s)
    print("Number of sub-strings with the same first and last characters:", count)


if __name__ == "__main__":
    main()
