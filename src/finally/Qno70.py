"""
Qno.70: Simulate a download and always show "Download finished" with finally.

Difficult words:
- simulate: imitate a real process.
"""

import time

try:
    total_parts = 5
    for part in range(1, total_parts + 1):
        print(f"Downloading part {part}/{total_parts}...")
        time.sleep(0.3)
except Exception as e:
    print("Download error:", e)
finally:
    print("Download finished")
