"""
Qno3 - Lottery Number Picker
Difficult words:
- lottery: game of chance with random numbers
- unique: no duplicates
"""

import random

# pick 6 unique numbers from 1 to 49
numbers = random.sample(range(1, 50), 6)
numbers.sort()
print("Lottery numbers:", numbers)
