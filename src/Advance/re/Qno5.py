"""
Qno5 - Date Finder
Difficult words:
- extract: pull out specific parts
- various formats: multiple possible styles
"""

import re

text = input("Enter text containing dates: ")

# Common formats: DD/MM/YYYY, DD-MM-YYYY, YYYY-MM-DD
pattern = r"\b(?:\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2})\b"

dates = re.findall(pattern, text)

print("Dates found:", dates if dates else "None")
