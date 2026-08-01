"""
Qno10 - Random Quiz Generator
Difficult words:
- quiz: short test
"""

import random

questions = [
    "What is the output of 2 + 2?",
    "Which keyword defines a function in Python?",
    "What data type is [1, 2, 3]?",
    "Which loop repeats while a condition is true?",
    "What does len() return?",
]

count = int(input("How many random questions? "))
count = max(1, min(count, len(questions)))

picked = random.sample(questions, count)
print("Quiz Questions:")
for i, q in enumerate(picked, start=1):
    print(f"{i}. {q}")
