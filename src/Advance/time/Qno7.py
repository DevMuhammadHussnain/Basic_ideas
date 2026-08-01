"""
Qno7 - Time Zone Checker using gmtime()
Difficult words:
- timezone: region with its own standard time
- UTC: Coordinated Universal Time (world reference time)
- gmtime: returns UTC time structure
"""

import time

utc_struct = time.gmtime()
utc_readable = time.strftime("%Y-%m-%d %H:%M:%S", utc_struct)
local_readable = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print(f"UTC time   : {utc_readable}")
print(f"Local time : {local_readable}")
