def find_palindromic_substrings(s):
    palindromic_substrings = []
    for length in range(1, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and len(substring) > 1:
                palindromic_substrings.append(substring)
    return palindromic_substrings

def main():
    s = input("Enter string to test: ")
    print(find_palindromic_substrings(s))

if __name__ == "__main__":
    main()