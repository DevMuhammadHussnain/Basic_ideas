"""
Qno8 - Compound Interest Calculator (math)

Compute compound growth using exponentiation.

Difficult words:
- principal: initial amount of money
- compound: growth added back for future growth
- exponentiation: raising to a power
"""

import math


def compound_amount(principal: float, rate: float, times_per_year: int, years: float) -> float:
    return principal * math.pow((1 + rate / times_per_year), times_per_year * years)


if __name__ == "__main__":
    p = float(input("Principal amount: "))
    r = float(input("Annual rate (%) : ")) / 100
    n = int(input("Compounds per year: "))
    t = float(input("Years: "))

    final = compound_amount(p, r, n, t)
    print(f"Final amount = {final:.2f}")
