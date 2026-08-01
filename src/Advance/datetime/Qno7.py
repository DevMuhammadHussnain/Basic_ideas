"""
Qno7 - Date Formatter (datetime)

Format current date/time in different styles.

Difficult words:
- format: specific display pattern
- timestamp: machine-friendly date-time value
- representation: way to show data
"""

from datetime import datetime


if __name__ == "__main__":
    now = datetime.now()
    print("ISO:", now.isoformat(timespec="seconds"))
    print("Style 1:", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("Style 2:", now.strftime("%d/%m/%Y"))
    print("Style 3:", now.strftime("%A, %B %d, %Y"))
