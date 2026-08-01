"""
Qno6 - Prime Number Estimator (math)

Check if a number is prime using sqrt limit.

Difficult words:
- prime: number divisible only by 1 and itself
- divisor: number that divides another exactly
- optimization: making method faster/more efficient
"""

import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    num = int(input("Enter integer: "))
    print("Prime" if is_prime(num) else "Not prime")
