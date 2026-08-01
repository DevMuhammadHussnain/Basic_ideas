"""
Qno.93: Use assert to ensure input is within a specific range.

Difficult words:
- range: min to max allowed interval.
"""

x = int(input("Enter number between 10 and 50: "))
assert 10 <= x <= 50, "Number must be between 10 and 50"
print("Number is in range")
