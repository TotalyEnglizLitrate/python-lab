"""
    Get a year from the user and check if it is a leap year and display the result.
"""


def check_leap_year(year):
    chk = tuple(map(lambda x: year % x, (4, 100, 400)))
    if chk[2] == True:
        return True
    elif chk[1] == True:
        return False
    elif chk[0] == True:
        return True
    
    return False

def main():
    year = int(input("Enter a year: "))
    print(f"{year} is{' ' if check_leap_year(year) else ' not '} a leap year")

if __name__ == "__main__":
    main()