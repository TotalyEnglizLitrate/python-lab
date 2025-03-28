# Aim:
- To explore strings in Python by writing programs for the following and executing them
t. Given a string, find the list of palindromic sub-strings without using built-in functions.
**Algorithm:**
1. **Input:** Get a string `s` from the user.
2. **Initialize List:** Create an empty list `palindromic_substrings` to store the palindromic substrings.
3. **Outer Loop (Length):** Iterate through possible substring lengths from 2 to the length of `s`.
4. **Inner Loop (Start Index):** Iterate through possible starting indices for substrings of the current length.
5. **Extract Substring:** Extract the substring `substring` from `s` using the current start index and length.
6. **Check for Palindrome:**
    - Create a reversed copy of `substring` without using built-in functions.
    - Compare `substring` with its reversed copy.
    - If they are equal, it's a palindrome.
7. **Append to List:** If the substring is a palindrome, append it to `palindromic_substrings`.
8. **Output:** Print the `palindromic_substrings` list.
**Code**:
```py
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
```
**Output**:![[Pasted image 20250324083907.png]]

u. List the number of sub-strings with the same first and last characters in a given
string.
**Algorithm:**
1. **Input:** Get a string `s` from the user.
2. **Initialize Count:** Set a counter `count` to 0.
3. **Outer Loop (Length):** Iterate through possible substring lengths from 1 to the length of `s`.
4. **Inner Loop (Start Index):** Iterate through possible starting indices for substrings of the current length.
5. **Extract Substring:** Extract the substring `substring` from `s` using the current start index and length.
6. **Check First and Last Characters:**
    - If the first character (`substring[0]`) is equal to the last character (`substring[-1]`), increment the `count`.
7. **Output:** Print the final `count`.
**Code**:
```py
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
```
**Output**:![[Pasted image 20250324085120.png]]
v. Break a given string into multiple lines with N characters each. Get the value of N
from the user.
**Algorithm:**
1. **Input:** Get the string `s` and the number of characters per line `N` from the user.
2. **Initialize Lines List:** Create an empty list `lines` to store the broken lines.
3. **Loop through String:** Iterate through the string `s` with a step size of `N`.
4. **Extract Substring:** Extract a substring of length `N` from `s` using the current index.
5. **Append to Lines:** Append the extracted substring to the `lines` list.
6. **Output:**
    - Iterate through the `lines` list.
    - Print each line along with its line number.
**Code:**
```py
def break_string_into_lines(s, n):
    lines = []
    for i in range(0, len(s), n):
        lines.append(s[i:i + n])
    return lines

def main():
    s = input("Enter the string: ")
    n = int(input("Enter the number of characters per line (N): "))
    lines = break_string_into_lines(s, n)
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line}")

if __name__ == "__main__":
    main()
```
**Output**:![[Pasted image 20250324085640.png]]
w. Sort the characters of a string based on their frequency of occurrence.
**Algorithm:**
1. **Input:** Get a string from the user.
2. **Count Character Frequencies:** Create a dictionary to store the frequency of each character in the string.
3. **Sort Characters:** Sort the characters based on their frequencies in ascending order.
4. **Output:** Print the sorted list of characters.
**Code**:
```py
from collections import Counter

def main():
    count = Counter(input("Enter a string: "))
    print(sorted(count, key=count.get))

if __name__ == "__main__":
    main()
```
**Output**:![[Pasted image 20250324090339.png]]
x. Concatenate two strings of the same length, without using built-in functions, such
that the characters of each string are placed alternately in the resultant string.
**Algorithm:**
1. **Input:** Get two strings `s1` and `s2` from the user.
2. **Check Lengths:** If the lengths of `s1` and `s2` are not equal, print an error message and stop.
3. **Initialize Result:** Create an empty string `result`.
4. **Loop Through Strings:** Iterate through the characters of `s1` and `s2` simultaneously.
5. **Append Characters:**
    - Append the current character from `s1` to `result`.
    - Append the current character from `s2` to `result`.
6. **Output:** Print the `result` string.
**Code**:
```py
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
```
**Output**:![[Pasted image 20250324090855.png]]

y. Encode a given string using Caesar's cipher, where each letter in a string is replaced by a letter some fixed number of positions down the alphabet. Get the alphabetic string and the number of places each letter is to be shifted from the user.
**Algorithm:**
1. **Input:** Get the string `s` and the shift value (number of positions) from the user.
2. **Initialize Result:** Create an empty string `result` to store the encoded string.
3. **Loop Through String:** Iterate through each character `char` in the input string `s`.
4. **Check if Alphabetic:**
    - If `char` is an alphabet:
        - Determine the ASCII offset: 65 for uppercase, 97 for lowercase.
        - Calculate the encoded character's ASCII value:
            - `(ord(char) - ascii_offset + shift) % 26 + ascii_offset`.
        - Convert the ASCII value back to a character using `chr()` and append it to `result`.
    - Else (if `char` is not alphabetic):
        - Append `char` directly to `result` (no encoding).
5. **Output:** Print the `result` string (the encoded string).
**Code**:
```py
def caesar_cipher(s, shift):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def main():
    s = input("Enter the string to encode: ")
    shift = int(input("Enter the number of places to shift each letter: "))

    encoded_string = caesar_cipher(s, shift)
    print("Encoded string:", encoded_string)

if __name__ == "__main__":
    main()
```
**Output**:![[Pasted image 20250324091300.png]]