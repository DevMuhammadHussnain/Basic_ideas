"""
Qno.54: Raise a custom exception if password is too short or lacks numbers/letters.

Difficult words:
- custom exception: user-defined error type.
- lacks: does not contain.
"""

class WeakPasswordError(Exception):
    pass


def validate_password(password):
    if len(password) < 6:
        raise WeakPasswordError("Password is too short.")
    if not any(ch.isdigit() for ch in password):
        raise WeakPasswordError("Password must include at least one number.")
    if not any(ch.isalpha() for ch in password):
        raise WeakPasswordError("Password must include at least one letter.")
    return True


pwd = input("Enter password: ")
try:
    if validate_password(pwd):
        print("Strong password")
except WeakPasswordError as e:
    print(e)
