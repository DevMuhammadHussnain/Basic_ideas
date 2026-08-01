"""
Qno9: Population vs Sample
Learn the difference and calculate statistics for both.

Difficult words:
- population: entire group of data
- sample: small part of population
"""

import statistics

population_data = [10, 12, 14, 16, 18, 20, 22, 24]
sample_data = [12, 16, 20, 24]

print("Population Data:", population_data)
print("Sample Data:", sample_data)

print("\nPopulation Mean:", statistics.mean(population_data))
print("Population Variance:", statistics.pvariance(population_data))
print("Population Std Dev:", statistics.pstdev(population_data))

print("\nSample Mean:", statistics.mean(sample_data))
print("Sample Variance:", statistics.variance(sample_data))
print("Sample Std Dev:", statistics.stdev(sample_data))
