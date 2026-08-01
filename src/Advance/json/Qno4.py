"""
Qno4 - JSON to Dictionary
Difficult words:
- dictionary: key-value data structure in Python
"""

import json

json_text = '{"name": "Ali", "age": 20, "skills": ["Python", "Git"]}'
python_dict = json.loads(json_text)

print("Dictionary:", python_dict)
print("Type:", type(python_dict).__name__)
