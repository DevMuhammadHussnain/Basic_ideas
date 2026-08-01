# Qno.22 (Return section duplicate in source text)
# Store data in array of size 10; return error if data is missing.
# Difficult words:
# - return error: send back a problem message from function

def collect_ten_items():
    arr = []
    for i in range(10):
        value = input(f"Enter value {i + 1}: ").strip()
        if value == "":
            return f"Error: Missing data at position {i + 1}"
        arr.append(value)
    return arr

result = collect_ten_items()
print(result)
