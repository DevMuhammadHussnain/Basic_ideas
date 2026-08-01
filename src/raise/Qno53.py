"""
Qno.53: Input a grade (0-100), and raise an error if out of range.

Difficult words:
- grade: score/marks.
- range: interval between minimum and maximum.
"""

def validate_grade(grade):
    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100.")
    return True


g = float(input("Enter grade: "))
try:
    if validate_grade(g):
        print("Valid grade")
except ValueError as e:
    print(e)
