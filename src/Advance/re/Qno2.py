"""
Qno2 - Phone Number Formatter
Difficult words:
- format: arrange text in a standard style
"""

import re

raw = input("Enter phone number (digits only or mixed): ")
digits = re.sub(r"\D", "", raw)  # remove non-digits

if len(digits) == 10:
    formatted = f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    print("Formatted:", formatted)
else:
    print("Please enter exactly 10 digits.")
