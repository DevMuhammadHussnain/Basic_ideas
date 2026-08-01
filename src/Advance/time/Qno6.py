"""
Qno6 - Time Spent Calculator
Difficult words:
- process: a task/program operation
"""

import time

print("Running a sample process...")
start = time.time()

# sample process
for _ in range(5):
    time.sleep(0.4)

end = time.time()
spent = end - start
print(f"Process took {spent:.2f} seconds")
