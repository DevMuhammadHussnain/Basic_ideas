"""
Qno1 - Email Validator
Difficult words:
- regex (regular expression): pattern for matching text
- validate: check if format is correct
"""

import re

email = input("Enter email: ")
pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.fullmatch(pattern, email):
    print("Valid email ✅")
else:
    print("Invalid email ❌")
