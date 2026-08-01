"""
Qno9 - Log File Parser
Difficult words:
- parse: analyze structured text
- error pattern: text style that indicates an error
"""

import re

file_path = "app.log"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    error_lines = [line.strip() for line in lines if re.search(r"\b(ERROR|CRITICAL|Exception)\b", line)]

    print(f"Found {len(error_lines)} error-related line(s):")
    for line in error_lines:
        print("-", line)

except FileNotFoundError:
    print(f"Log file not found: {file_path}")
