"""
Qno.104: Use yield to create a generator function that produces a sequence of numbers.

Difficult words:
- yield: returns value one-by-one from generator.
- generator: function that produces sequence lazily.
"""


def number_sequence(n):
    for i in range(1, n + 1):
        yield i


for num in number_sequence(10):
    print(num)
