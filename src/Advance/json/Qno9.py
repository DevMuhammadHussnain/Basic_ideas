"""
Qno9 - JSON File Writer
Difficult words:
- serialize: convert Python object to storable text format
"""

import json

data = {
    "course": "Python Basics",
    "level": "Beginner",
    "students": 35,
    "topics": ["variables", "loops", "functions"]
}

with open("output.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("Data written to output.json")
