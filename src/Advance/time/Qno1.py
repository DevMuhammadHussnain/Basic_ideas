"""
Qno1 - Stopwatch
Difficult words:
- stopwatch: a tool to measure elapsed (passed) time
- elapsed: time that has gone by
"""

import time

print("Stopwatch started. Press Enter to stop...")
start_time = time.time()  # current time in seconds
input()
end_time = time.time()

elapsed_seconds = end_time - start_time
print(f"Elapsed time: {elapsed_seconds:.2f} seconds")
