"""
Qno3: Data Outlier Detection
Identify outliers in a dataset using standard deviation.

Difficult words:
- outlier: a value very far from most values
- threshold: a limit used for checking
"""

import statistics

data = [10, 12, 11, 13, 12, 100, 11, 10, 9]
mean_val = statistics.mean(data)
std_dev = statistics.pstdev(data)

# Using 2 standard deviations as threshold
threshold = 2
outliers = [x for x in data if abs(x - mean_val) > threshold * std_dev]

print("Data:", data)
print("Mean:", mean_val)
print("Population Std Dev:", std_dev)
print("Outliers:", outliers)
