"""
Qno9 - Hypotenuse Finder (math)

Use math.hypot() directly for two sides.

Difficult words:
- direct: done in a simple/straight way
- Euclidean: standard geometry distance style
- concise: short but clear
"""

import math


if __name__ == "__main__":
    x = float(input("Enter side 1: "))
    y = float(input("Enter side 2: "))
    print(f"Hypotenuse = {math.hypot(x, y):.6f}")
