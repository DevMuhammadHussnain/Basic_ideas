"""
Qno.88: Track event count with nonlocal in nested function.

Difficult words:
- event: an action/occurrence.
"""

def event_tracker():
    event_count = 0

    def track(event_name):
        nonlocal event_count
        event_count += 1
        print(f"Event {event_count}: {event_name}")

    return track


track = event_tracker()
track("login")
track("click")
track("logout")
