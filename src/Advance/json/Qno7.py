"""
Qno7 - Nested JSON Reader
Difficult words:
- nested: inside another structure
- parse: read and understand structured text
"""

import json

json_text = '''
{
  "user": {
    "name": "Ayesha",
    "address": {
      "city": "Karachi",
      "zip": "74000"
    },
    "skills": ["Python", "Data Analysis"]
  }
}
'''

data = json.loads(json_text)

print("Name:", data["user"]["name"])
print("City:", data["user"]["address"]["city"])
print("First skill:", data["user"]["skills"][0])
