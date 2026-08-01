"""
Qno.69: Use finally to reset a timer even if an error occurs.

Difficult words:
- reset: set back to initial state.
"""

import time

start_time = None
try:
    start_time = time.time()
    n = int(input("Enter a positive integer: "))
    if n < 0:
        raise ValueError("Negative number not allowed")
    print("Processing number:", n)
except ValueError as e:
    print(e)
finally:
    end_time = time.time()
    if start_time is not None:
        print("Elapsed seconds:", round(end_time - start_time, 4))
    print("Timer reset/finished")
