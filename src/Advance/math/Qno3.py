"""
Qno3 - Simple Trig Tool (math)

Compute sin, cos, tan for angle in degrees.

Difficult words:
- trigonometry: math of angles and sides
- radians: angle unit used by math module
- conversion: changing from one form to another
"""

import math


def trig_values(degrees: float):
    rad = math.radians(degrees)
    return math.sin(rad), math.cos(rad), math.tan(rad)


if __name__ == "__main__":
    d = float(input("Enter angle in degrees: "))
    s, c, t = trig_values(d)
    print(f"sin({d}) = {s:.6f}")
    print(f"cos({d}) = {c:.6f}")
    print(f"tan({d}) = {t:.6f}")
