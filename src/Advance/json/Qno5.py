"""
Qno5 - JSON Formatter
Difficult words:
- pretty-print: display in readable formatted style
- indent: left spacing for structure
"""

import json

raw_json = '{"name":"Sara","age":22,"city":"Lahore","skills":["Python","SQL"]}'

data = json.loads(raw_json)
formatted = json.dumps(data, indent=4, sort_keys=True)

print("Formatted JSON:")
print(formatted)
