"""
Qno.55: Raise an error if file name doesn’t end with .txt or .csv.

Difficult words:
- extension: ending part of a file name (e.g., .txt).
"""

def validate_filename(filename):
    if not (filename.endswith(".txt") or filename.endswith(".csv")):
        raise ValueError("File name must end with .txt or .csv")
    return True


name = input("Enter file name: ")
try:
    if validate_filename(name):
        print("Valid file name")
except ValueError as e:
    print(e)
