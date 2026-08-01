"""
Qno2 - Random Password Generator
Difficult words:
- secure: hard to guess or break
- password: secret text for authentication
"""

import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+"
all_chars = letters + numbers + symbols

length = int(input("Enter password length: "))
password = "".join(random.choice(all_chars) for _ in range(length))

print("Generated password:", password)
