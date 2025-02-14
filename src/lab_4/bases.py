"""
Obtain 2 decimal numbers from the user, display them in binary, octal, and
hexadecimal forms, perform the logical operations (and, or, not, left and right shift)
and print the results in binary and decimal forms.
"""

def get_user_input():
    num1 = int(input("Enter first decimal number: "))
    num2 = int(input("Enter second decimal number: "))
    return num1, num2

def display_base_forms(num1, num2):
    print(f"Binary form of {num1}: {bin(num1)}")
    print(f"Octal form of {num1}: {oct(num1)}")
    print(f"Hexadecimal form of {num1}: {hex(num1)}")
    print(f"Binary form of {num2}: {bin(num2)}")
    print(f"Octal form of {num2}: {oct(num2)}")
    print(f"Hexadecimal form of {num2}: {hex(num2)}")

def perform_logical_operations(num1, num2):
    and_result = num1 & num2
    or_result = num1 | num2
    not_result1 = ~num1
    not_result2 = ~num2
    left_shift_result1 = num1 << 1
    left_shift_result2 = num2 << 1
    right_shift_result1 = num1 >> 1
    right_shift_result2 = num2 >> 1
    print(f"And operation: {bin(and_result)} ({and_result})")
    print(f"Or operation: {bin(or_result)} ({or_result})")
    print(f"Not operation on {num1}: {bin(not_result1)} ({not_result1})")
    print(f"Not operation on {num2}: {bin(not_result2)} ({not_result2})")
    print(f"Left shift operation on {num1}: {bin(left_shift_result1)} ({left_shift_result1})")
    print(f"Left shift operation on {num2}: {bin(left_shift_result2)} ({left_shift_result2})")
    print(f"Right shift operation on {num1}: {bin(right_shift_result1)} ({right_shift_result1})")
    print(f"Right shift operation on {num2}: {bin(right_shift_result2)} ({right_shift_result2})")

def main():
    num1, num2 = get_user_input()
    display_base_forms(num1, num2)
    perform_logical_operations(num1, num2)

if __name__ == "__main__":
    main()