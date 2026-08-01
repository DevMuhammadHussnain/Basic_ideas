"""
Qno4: Percentile Calculator
Calculate specific percentiles in a dataset.

Difficult words:
- percentile: value below which a percentage of data falls
- interpolate: estimate between two values
"""

import statistics

def percentile(data, p):
    """Return pth percentile (0-100) using linear interpolation."""
    if not data:
        raise ValueError("Data cannot be empty")
    if not 0 <= p <= 100:
        raise ValueError("Percentile must be between 0 and 100")

    sorted_data = sorted(data)
    k = (len(sorted_data) - 1) * (p / 100)
    f = int(k)
    c = min(f + 1, len(sorted_data) - 1)

    if f == c:
        return sorted_data[f]

    # linear interpolation between sorted_data[f] and sorted_data[c]
    d0 = sorted_data[f] * (c - k)
    d1 = sorted_data[c] * (k - f)
    return d0 + d1

data = [5, 7, 8, 12, 15, 18, 20, 22, 30]
print("Data:", data)
print("25th percentile:", percentile(data, 25))
print("50th percentile:", percentile(data, 50))
print("90th percentile:", percentile(data, 90))
print("Median using statistics:", statistics.median(data))
