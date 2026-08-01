"""
Q10: CSV Data Exporter – Export data to a CSV file from an external source.

Difficult words:
- export: save data out to another file/system
- external source: data coming from outside this script
"""

import csv

# Simulated external source (for example: database result)
records = [
    {"id": 1, "product": "Pen", "price": 10},
    {"id": 2, "product": "Notebook", "price": 50},
]

with open("export.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["id", "product", "price"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print("Export complete: export.csv")
