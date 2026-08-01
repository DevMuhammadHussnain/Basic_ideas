"""
Qno2 - JSON Data Validator
Difficult words:
- validate: check if data is correct
- structure: arrangement/organization of data
"""

import json

json_text = input("Enter JSON text: ")

try:
    parsed = json.loads(json_text)
    print("Valid JSON ✅")
    print("Parsed type:", type(parsed).__name__)
except json.JSONDecodeError as error:
    print("Invalid JSON ❌")
    print("Reason:", error)
