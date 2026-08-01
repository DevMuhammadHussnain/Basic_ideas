# Qno.48
# Simulate basic alarm system with booleans.
# Difficult words:
# - motion_detected: movement found by sensor
# - alarm_on: alarm state

motion_detected = input("Motion detected? (yes/no): ").lower() == "yes"
password_entered = input("Password entered? (yes/no): ").lower() == "yes"

alarm_on = motion_detected and (not password_entered)
print("Alarm ON" if alarm_on else "Alarm OFF")
