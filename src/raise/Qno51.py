"""
Qno.51: Create a function that raises a ValueError if the user's age is less than 0.

Difficult words:
- raise: to trigger an error intentionally.
- ValueError: an error for invalid value type/content.
"""

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be less than 0.")
    return True


age_input = int(input("Enter age: "))
try:
    if validate_age(age_input):
        print("Valid age")
except ValueError as e:
    print(e)
