# Qno.22
# Store data in array of size 10; if data is missing, show error.
# Difficult words:
# - size: fixed number of positions
# - missing: not provided / empty

arr = []

for i in range(10):
    value = input(f"Enter value for position {i + 1}: ").strip()
    if value == "":
        print(f"Error: Data is missing at position {i + 1}")
    arr.append(value)

print("Stored data:", arr)
