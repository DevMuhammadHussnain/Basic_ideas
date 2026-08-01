"""
Qno6 - Leap Year Checker (datetime)

Check if a year is leap year.

Difficult words:
- leap year: year with 366 days
- divisible: can be divided exactly
- Gregorian: widely used calendar system
"""

from datetime import datetime


def is_leap(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


if __name__ == "__main__":
    text = input("Enter year: ").strip()
    if not text.isdigit():
        print("Invalid year.")
    else:
        y = int(text)
        print(f"{y} is leap year" if is_leap(y) else f"{y} is not leap year")
        print("Current datetime:", datetime.now())
