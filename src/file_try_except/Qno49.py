# Qno.49
# Try to read a specific line in a file.
# Difficult words:
# - specific: exact, particular
# - line: one row of text in a file

file_name = input("Enter file name: ")
line_number = int(input("Enter line number to read: "))

try:
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if 1 <= line_number <= len(lines):
            print("Line:", lines[line_number - 1].rstrip("\n"))
        else:
            print("Error: Line number out of range")
except FileNotFoundError:
    print("Error: File not found")
