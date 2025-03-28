def break_string_into_lines(s, n):
    lines = []
    for i in range(0, len(s), n):
        lines.append(s[i : i + n])
    return lines


def main():
    s = input("Enter the string: ")
    n = int(input("Enter the number of characters per line (N): "))
    lines = break_string_into_lines(s, n)
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line}")


if __name__ == "__main__":
    main()
