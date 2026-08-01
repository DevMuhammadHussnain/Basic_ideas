# Qno.21
# Store data in memory in reverse order and print in reverse order.
# Difficult words:
# - memory: where program stores data temporarily
# - reverse order: opposite order (last to first)

data = []

for i in range(5):
    value = input(f"Enter value {i + 1}: ")
    # insert at start to store in reverse directly
    data.insert(0, value)

print("Data in reverse order:")
for item in data:
    print(item)
