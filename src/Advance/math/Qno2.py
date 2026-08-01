"""
Qno2 - Pythagorean Theorem Solver (math)

Find missing side in right triangle.

Difficult words:
- hypotenuse: longest side in right triangle
- theorem: proven mathematical statement
- non-negative: zero or positive
"""

import math


def find_hypotenuse(a: float, b: float) -> float:
    return math.sqrt(a * a + b * b)


def find_leg(h: float, a: float) -> float:
    value = h * h - a * a
    if value < 0:
        raise ValueError("Hypotenuse must be largest side.")
    return math.sqrt(value)


if __name__ == "__main__":
    mode = input("Find (h)ypotenuse or (l)eg? ").strip().lower()
    if mode == "h":
        a = float(input("Side a: "))
        b = float(input("Side b: "))
        print(f"Hypotenuse = {find_hypotenuse(a, b):.4f}")
    elif mode == "l":
        h = float(input("Hypotenuse h: "))
        a = float(input("Known leg a: "))
        try:
            print(f"Missing leg = {find_leg(h, a):.4f}")
        except ValueError as err:
            print(err)
    else:
        print("Invalid choice.")
