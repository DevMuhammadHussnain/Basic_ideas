"""
Qno4 - Current Time Display
Difficult words:
- continuously: without stopping
- system time: computer's current local time
"""

import time

print("Showing current time (Ctrl+C to stop):")

try:
    while True:
        # %H:%M:%S => hour:minute:second
        current = time.strftime("%H:%M:%S", time.localtime())
        print(current)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped by user.")
