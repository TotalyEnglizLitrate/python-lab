"""
Write a program using tuples to record the marks achieved by 22 students in the
course. Find the highest marks, lowest marks, average marks, and the total
number of failed candidates in the course. Using List comprehension, filter out
the failed candidate scores. You are free to use LOOPs, Conditional Logic, and
built-in functions.
"""

from json import dumps


PASS_THRESHOLD = 40


if __name__ == "__main__":
    marks = [
        (input(f"Enter name of student {i+ 1}: "), int(input(f"Enter marks of student: ")), print())[:2] 
        for i in range(22)
        ]
    
    max_marks = max(marks, key=lambda s:s[1])
    min_marks = min(marks, key=lambda s:s[1])
    avg_marks = sum((s[1] for s in marks)) / 22

    failed_students = [s for s in marks if s[1] < PASS_THRESHOLD]

    print(f"{min_marks=}, {max_marks=}, {avg_marks=}")
    print(f"no. of students below pass mark threshold: {len(failed_students)}")
    print(dumps(failed_students, indent=2))