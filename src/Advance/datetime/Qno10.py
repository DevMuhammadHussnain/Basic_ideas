"""
Qno10 - Localized Date Display (datetime)

Show date in local style using common format patterns.

Difficult words:
- localized: adapted for user region/style
- locale: regional rules for language/date/time
- fallback: backup method if primary is unavailable
"""

from datetime import datetime


if __name__ == "__main__":
    now = datetime.now()
    # Without extra modules, we use several common display styles.
    print("US style    :", now.strftime("%m/%d/%Y %I:%M %p"))
    print("EU style    :", now.strftime("%d/%m/%Y %H:%M"))
    print("ISO style   :", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("Readable    :", now.strftime("%A, %d %B %Y"))
