"""
Qno8: Random Sampling
Generate random samples and analyze mean/median.

Difficult words:
- sampling: selecting some values from a larger group
- random: chosen without a fixed pattern
"""

import random
import statistics

population = list(range(1, 101))  # numbers from 1 to 100
sample = random.sample(population, 10)

print("Population size:", len(population))
print("Sample:", sample)
print("Sample Mean:", statistics.mean(sample))
print("Sample Median:", statistics.median(sample))
