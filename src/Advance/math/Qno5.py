"""
Qno5 - Factorial Finder (math)

Calculate factorial using math.factorial().

Difficult words:
- factorial: product of all positive integers up to n
- integer: whole number (no decimal)
- validation: checking input correctness
"""

import math


if __name__ == "__main__":
    text = input("Enter non-negative integer: ").strip()
    if not text.isdigit():
        print("Invalid input.")
    else:
        n = int(text)
        print(f"{n}! = {math.factorial(n)}")
