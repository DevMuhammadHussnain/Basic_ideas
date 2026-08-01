"""
Qno10 - JSON Merger
Difficult words:
- merge: combine multiple parts into one
"""

import json

file1 = "file1.json"
file2 = "file2.json"
output_file = "merged.json"

try:
    with open(file1, "r", encoding="utf-8") as f1:
        data1 = json.load(f1)

    with open(file2, "r", encoding="utf-8") as f2:
        data2 = json.load(f2)

    # Basic merge approach depending on type
    if isinstance(data1, dict) and isinstance(data2, dict):
        merged = {**data1, **data2}
    elif isinstance(data1, list) and isinstance(data2, list):
        merged = data1 + data2
    else:
        merged = {"file1": data1, "file2": data2}

    with open(output_file, "w", encoding="utf-8") as out:
        json.dump(merged, out, indent=4)

    print(f"Merged data saved to {output_file}")

except FileNotFoundError as error:
    print("Missing file:", error)
except json.JSONDecodeError:
    print("One of the files has invalid JSON.")
