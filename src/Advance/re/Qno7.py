"""
Qno7 - IP Address Extractor
Difficult words:
- IP address: numeric network address (e.g., 192.168.1.1)
"""

import re

text = input("Enter text: ")

# Basic IPv4 pattern
pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
ips = re.findall(pattern, text)

print("IP addresses found:", ips if ips else "None")
