"""
Qno4 - Random Sentence Generator
Difficult words:
- generate: create automatically
"""

import random

subjects = ["The cat", "A student", "My friend", "The robot"]
verbs = ["eats", "writes", "builds", "finds"]
objects = ["a sandwich", "Python code", "a project", "a solution"]

sentence = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."
print(sentence)
