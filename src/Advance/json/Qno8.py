"""
Qno8 - JSON Search
Difficult words:
- key: the label in key-value pair
- value: the data paired with key
"""

import json

file_path = "sample.json"
search_key = input("Enter key to search: ")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    def find_key(obj, target_key):
        """Recursively search target_key in nested JSON-like objects."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == target_key:
                    return v
                result = find_key(v, target_key)
                if result is not None:
                    return result
        elif isinstance(obj, list):
            for item in obj:
                result = find_key(item, target_key)
                if result is not None:
                    return result
        return None

    result = find_key(data, search_key)

    if result is not None:
        print(f"Found: {search_key} = {result}")
    else:
        print("Key not found.")

except FileNotFoundError:
    print(f"File not found: {file_path}")
except json.JSONDecodeError:
    print("Invalid JSON format in file.")
