"""
Qno1 - Area Calculator (math)

Compute area of circle, rectangle, triangle.

Difficult words:
- radius: distance from center to edge of circle
- formula: math rule for calculation
- precision: level of exactness
"""

import math


def area_circle(radius: float) -> float:
    return math.pi * radius * radius


def area_rectangle(length: float, width: float) -> float:
    return length * width


def area_triangle(base: float, height: float) -> float:
    return 0.5 * base * height


if __name__ == "__main__":
    print("Choose shape: circle / rectangle / triangle")
    shape = input("Shape: ").strip().lower()

    if shape == "circle":
        r = float(input("Radius: "))
        print(f"Area = {area_circle(r):.4f}")
    elif shape == "rectangle":
        l = float(input("Length: "))
        w = float(input("Width: "))
        print(f"Area = {area_rectangle(l, w):.4f}")
    elif shape == "triangle":
        b = float(input("Base: "))
        h = float(input("Height: "))
        print(f"Area = {area_triangle(b, h):.4f}")
    else:
        print("Invalid shape.")
