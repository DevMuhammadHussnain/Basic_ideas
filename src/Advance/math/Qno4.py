"""
Qno4 - Logarithm Converter (math)

Convert between natural log, log10 and custom base log.

Difficult words:
- logarithm: inverse of exponent operation
- natural log: log with base e
- custom base: user-defined base value
"""

import math


def show_logs(value: float, base: float) -> None:
    if value <= 0 or base <= 0 or base == 1:
        print("Value must be > 0 and base must be > 0 and not 1.")
        return

    print(f"ln({value}) = {math.log(value):.6f}")
    print(f"log10({value}) = {math.log10(value):.6f}")
    print(f"log base {base} of {value} = {math.log(value, base):.6f}")


if __name__ == "__main__":
    v = float(input("Enter positive value: "))
    b = float(input("Enter custom base: "))
    show_logs(v, b)
