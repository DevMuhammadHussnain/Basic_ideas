"""
Qno1 - JSON File Reader
Difficult words:
- JSON: JavaScript Object Notation (text data format)
- load: read data from file into Python object
"""

import json

file_path = "sample.json"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    print("JSON data loaded successfully:")
    print(data)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except json.JSONDecodeError:
    print("Invalid JSON format in file.")
