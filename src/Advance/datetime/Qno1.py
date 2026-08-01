"""
Qno1 - Date Difference Calculator (datetime)

Find difference between two dates.

Difficult words:
- difference: gap between two values
- parse: convert text into date object
- duration: amount of elapsed time
"""

from datetime import datetime


def date_diff(date1: str, date2: str) -> int:
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)


if __name__ == "__main__":
    a = input("Enter first date (YYYY-MM-DD): ").strip()
    b = input("Enter second date (YYYY-MM-DD): ").strip()
    try:
        print(f"Difference: {date_diff(a, b)} day(s)")
    except ValueError:
        print("Invalid date format.")
