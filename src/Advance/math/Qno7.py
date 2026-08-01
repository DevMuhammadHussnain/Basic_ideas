"""
Qno7 - Decimal to Radian Converter (math)

Convert degrees to radians and radians to degrees.

Difficult words:
- degree: common angle unit (0 to 360 in full turn)
- radian: mathematical angle unit
- reciprocal conversion: two-way conversion
"""

import math


if __name__ == "__main__":
    mode = input("Convert (d)egrees->radians or (r)adians->degrees? ").strip().lower()
    value = float(input("Enter value: "))

    if mode == "d":
        print(f"Radians = {math.radians(value):.6f}")
    elif mode == "r":
        print(f"Degrees = {math.degrees(value):.6f}")
    else:
        print("Invalid mode.")
