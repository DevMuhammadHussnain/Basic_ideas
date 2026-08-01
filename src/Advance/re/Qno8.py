"""
Qno8 - Word Counter using regex
Difficult words:
- occurrence: how many times something appears
"""

import re

sentence = input("Enter sentence: ")
word = input("Enter word to count: ")

# \b means word boundary so we match full word
pattern = rf"\b{re.escape(word)}\b"
count = len(re.findall(pattern, sentence, flags=re.IGNORECASE))

print(f"'{word}' occurred {count} time(s).")
