# Qno.44
# Simulate traffic light system with boolean conditions.
# Difficult words:
# - pedestrian: person walking on road

light = input("Enter light color (green/red/yellow): ").lower()
pedestrian = input("Is pedestrian crossing? (yes/no): ").lower() == "yes"

if light == "green" and not pedestrian:
    print("Go")
else:
    print("Stop")
