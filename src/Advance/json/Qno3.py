"""
Qno3 - JSON-to-CSV Converter
Difficult words:
- convert: change from one format to another
- CSV: Comma-Separated Values (table-like text format)
"""

import json
import csv

input_json = "data.json"
output_csv = "data.csv"

try:
    with open(input_json, "r", encoding="utf-8") as file:
        records = json.load(file)

    if not isinstance(records, list) or not records:
        print("JSON must be a non-empty list of objects.")
    else:
        headers = records[0].keys()
        with open(output_csv, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(records)
        print(f"Converted {input_json} -> {output_csv}")
except FileNotFoundError:
    print(f"File not found: {input_json}")
except json.JSONDecodeError:
    print("Invalid JSON in input file.")
