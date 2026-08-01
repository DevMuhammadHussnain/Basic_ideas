"""
Qno.57: Create a custom InvalidEmailError and raise it if email is missing @.

Difficult words:
- custom: made by programmer for specific need.
- missing: not present.
"""

class InvalidEmailError(Exception):
    pass


def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Email must contain '@'.")
    return True


email_input = input("Enter email: ")
try:
    if validate_email(email_input):
        print("Valid email")
except InvalidEmailError as e:
    print(e)
