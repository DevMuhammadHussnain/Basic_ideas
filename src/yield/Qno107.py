"""
Qno.107: Use yield to create a generator that produces prime numbers.

Difficult words:
- prime number: number > 1 with only 1 and itself as factors.
- factor: number that divides another exactly.
"""


def prime_generator(limit):
    for num in range(2, limit + 1):
        is_prime = True
        for d in range(2, int(num ** 0.5) + 1):
            if num % d == 0:
                is_prime = False
                break
        if is_prime:
            yield num


for p in prime_generator(50):
    print(p)
