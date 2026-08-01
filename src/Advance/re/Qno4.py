"""
Qno4 - Text Searcher
Difficult words:
- pattern: text form to search
- phrase: group of words
"""

import re

text = input("Enter text: ")
pattern = input("Enter regex pattern to search: ")

matches = re.findall(pattern, text)

if matches:
    print("Matches found:", matches)
else:
    print("No matches found.")
