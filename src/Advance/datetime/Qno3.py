"""
Qno3 - Age Calculator (datetime)

Calculate age from birthdate.

Difficult words:
- birthdate: date of birth
- anniversary: yearly repeat of date
- subtract: take one value away from another
"""

from datetime import date, datetime


def calculate_age(birth: date, today: date) -> int:
    years = today.year - birth.year
    if (today.month, today.day) < (birth.month, birth.day):
        years -= 1
    return years


if __name__ == "__main__":
    text = input("Enter birthdate (YYYY-MM-DD): ").strip()
    try:
        b = datetime.strptime(text, "%Y-%m-%d").date()
        t = date.today()
        print(f"Age: {calculate_age(b, t)}")
    except ValueError:
        print("Invalid birthdate format.")
