"""
Qno10 - Data Masker
Difficult words:
- sensitive information: private/important data
- mask: hide part of information
"""

import re

text = input("Enter text with card number: ")

# Mask 16-digit card numbers written as 1234-5678-9012-3456 or 1234567890123456
pattern = r"\b(?:\d{4}[- ]?){3}\d{4}\b"

def hide_card(match):
    card = re.sub(r"\D", "", match.group())
    return "****-****-****-" + card[-4:]

masked_text = re.sub(pattern, hide_card, text)
print("Masked text:", masked_text)
