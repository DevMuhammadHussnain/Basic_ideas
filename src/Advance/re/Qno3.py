"""
Qno3 - Password Strength Checker
Difficult words:
- criteria: required conditions
- strength: how secure/strong a password is
"""

import re

password = input("Enter password: ")

checks = {
    "at least 8 characters": r".{8,}",
    "one uppercase letter": r"[A-Z]",
    "one lowercase letter": r"[a-z]",
    "one digit": r"\d",
    "one special character": r"[^A-Za-z0-9]"
}

failed = [name for name, pat in checks.items() if not re.search(pat, password)]

if not failed:
    print("Strong password ✅")
else:
    print("Weak password ❌")
    print("Missing:")
    for item in failed:
        print("-", item)
