"""
    Obtain the marks secured by a student in Maths, Physics, Chemistry, Computer Science, and English, out of 100, and calculate their average. Check the range within which the average mark falls and display the appropriate grade. (A+ grade - 90 to 100, A grade - 80 to 90, B+ grade - 70 to 80, B grade - 60 to 70, C grade - 50 to 60, D grade - 40 to 50, F grade - less than 40)
"""

def get_user_input():
    maths = float(input("Enter marks in Maths: "))
    physics = float(input("Enter marks in Physics: "))
    chemistry = float(input("Enter marks in Chemistry: "))
    computer_science = float(input("Enter marks in Computer Science: "))
    english = float(input("Enter marks in English: "))
    return maths, physics, chemistry, computer_science, english

def check_grade(average):
    if average >= 90 and average <= 100:
        print(f"Average mark: {average:.2f}, Grade: A+")
    elif average >= 80 and average < 90:
        print(f"Average mark: {average:.2f}, Grade: A")
    elif average >= 70 and average < 80:
        print(f"Average mark: {average:.2f}, Grade: B+")
    elif average >= 60 and average < 70:
        print(f"Average mark: {average:.2f}, Grade: B")
    elif average >= 50 and average < 60:
        print(f"Average mark: {average:.2f}, Grade: C")
    elif average >= 40 and average < 50:
        print(f"Average mark: {average:.2f}, Grade: D")
    else:
        print(f"Average mark: {average:.2f}, Grade: F")

def main():
    maths, physics, chemistry, computer_science, english = marks = get_user_input()
    average = sum(marks) / len(marks)
    check_grade(average)

if __name__ == "__main__":
    main()