"""
Qno.65: Open a file, read it, and close it using finally.

Difficult words:
- finally: block that always runs after try/except.
"""

f = None
try:
    f = open("sample.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    if f is not None:
        f.close()
    print("File handling finished")
