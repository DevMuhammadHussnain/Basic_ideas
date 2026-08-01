"""
Qno.105: Use yield to create an infinite generator that produces Fibonacci numbers.

Difficult words:
- infinite: without fixed end.
- Fibonacci: sequence where next = sum of previous two.
"""


def fibonacci_infinite():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci_infinite()
for _ in range(10):
    print(next(gen))
