"""
Qno4 - Day of the Week Finder (datetime)

Find weekday name for a given date.

Difficult words:
- weekday: day name (Monday, Tuesday, etc.)
- format code: pattern string for date text
- locale: regional language/date style setting
"""

from datetime import datetime


if __name__ == "__main__":
    text = input("Enter date (YYYY-MM-DD): ").strip()
    try:
        d = datetime.strptime(text, "%Y-%m-%d")
        print("Day:", d.strftime("%A"))
    except ValueError:
        print("Invalid date format.")
