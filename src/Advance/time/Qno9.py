"""
Qno9 - Performance Benchmarker
Difficult words:
- benchmarker: tool to measure performance/speed
- code block: a group of statements
"""

import time

start = time.perf_counter()  # high-precision timer

# code block to measure
total = 0
for i in range(1, 1000001):
    total += i

end = time.perf_counter()

print(f"Result: {total}")
print(f"Execution time: {end - start:.6f} seconds")
