"""
Qno5 - Interval Logger
Difficult words:
- interval: fixed gap between events
- logger/log: record information over time
"""

import time

interval = int(input("Enter interval in seconds: "))
count = int(input("How many logs to print: "))

for i in range(1, count + 1):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"Log {i}: {now}")
    if i != count:
        time.sleep(interval)
