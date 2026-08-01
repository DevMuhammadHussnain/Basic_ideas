"""
Qno6 - HTML Tag Extractor
Difficult words:
- tag: markup element like <p> or </div>
- extractor: tool that collects specific parts
"""

import re

html = input("Enter HTML string: ")

# Finds opening/closing tags, optionally with attributes
pattern = r"<\/?[A-Za-z][A-Za-z0-9]*(?:\s+[^<>]*)?>"
tags = re.findall(pattern, html)

print("HTML tags:", tags if tags else "None")
