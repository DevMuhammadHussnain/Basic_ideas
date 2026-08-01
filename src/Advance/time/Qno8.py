"""
Qno8 - Countdown to a Specific Future Time
Difficult words:
- specific: exact, clearly defined
- future time: time that has not happened yet
"""

import time

# User enters seconds from now for simplicity
future_after = int(input("Countdown for how many seconds from now? "))
target = time.time() + future_after

while True:
    remaining = int(target - time.time())
    if remaining <= 0:
        print("Reached the target time!")
        break
    print(f"Remaining: {remaining} second(s)")
    time.sleep(1)
