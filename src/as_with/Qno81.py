"""
Qno.81: Use with open() to read files, ensuring auto-close.

Difficult words:
- context manager: tool that manages setup/cleanup automatically.
"""

try:
    with open("sample.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("sample.txt not found")
