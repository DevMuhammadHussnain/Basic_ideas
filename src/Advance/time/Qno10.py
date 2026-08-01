"""
Qno10 - Daylight Saving Checker
Difficult words:
- daylight saving time (DST): clock shift used in some regions
- tm_isdst: field showing DST status (1 yes, 0 no, -1 unknown)
"""

import time

local = time.localtime()

if local.tm_isdst == 1:
    print("Current local time is in Daylight Saving Time (DST).")
elif local.tm_isdst == 0:
    print("Current local time is NOT in Daylight Saving Time (DST).")
else:
    print("DST information is unknown for this system/time.")
