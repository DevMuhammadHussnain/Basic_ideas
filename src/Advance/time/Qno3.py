"""
Qno3 - Timer (Countdown in seconds)
Difficult words:
- countdown: counting backwards to zero
- alert: a notification message
"""

import time

seconds = int(input("Set timer (seconds): "))

while seconds > 0:
    print(f"Time left: {seconds} second(s)")
    time.sleep(1)
    seconds -= 1

print("Time is up! Alert!")
