"""
Qno2 - Time Zone Converter (datetime)

Convert time between two UTC offsets.

Difficult words:
- timezone: region with specific standard time
- offset: difference from UTC in hours
- aware datetime: datetime object with timezone info
"""

from datetime import datetime, timedelta, timezone


def parse_offset(hours_text: str) -> timezone:
    hours = int(hours_text)
    return timezone(timedelta(hours=hours))


if __name__ == "__main__":
    time_text = input("Enter time (YYYY-MM-DD HH:MM): ").strip()
    from_off = input("From UTC offset (e.g., 5 or -4): ").strip()
    to_off = input("To UTC offset (e.g., 0 or 9): ").strip()

    try:
        base = datetime.strptime(time_text, "%Y-%m-%d %H:%M")
        src_tz = parse_offset(from_off)
        dst_tz = parse_offset(to_off)
        src_time = base.replace(tzinfo=src_tz)
        dst_time = src_time.astimezone(dst_tz)
        print("Converted:", dst_time.strftime("%Y-%m-%d %H:%M %Z%z"))
    except ValueError:
        print("Invalid input.")
