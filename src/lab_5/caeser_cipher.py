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
