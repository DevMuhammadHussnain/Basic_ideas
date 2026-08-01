"""
Qno5: Variance Finder
Compute the variance of a dataset.

Difficult words:
- variance: average squared distance from mean
- squared: multiplied by itself
"""

import statistics

data = [14, 15, 16, 17, 18, 19]

sample_variance = statistics.variance(data)
population_variance = statistics.pvariance(data)

print("Data:", data)
print("Sample Variance:", sample_variance)
print("Population Variance:", population_variance)
