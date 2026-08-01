"""
Qno7: Data Normalization
Normalize data using z-scores or min-max scaling.

Difficult words:
- normalize: convert values to a common scale
- z-score: number of standard deviations from mean
- min-max scaling: rescale data to 0..1 range
"""

import statistics

data = [10, 20, 30, 40, 50]

mean_val = statistics.mean(data)
std_dev = statistics.pstdev(data)

z_scores = [(x - mean_val) / std_dev if std_dev != 0 else 0 for x in data]

min_val = min(data)
max_val = max(data)
min_max_scaled = [(x - min_val) / (max_val - min_val) if max_val != min_val else 0 for x in data]

print("Original Data:", data)
print("Z-scores:", z_scores)
print("Min-Max Scaled:", min_max_scaled)
