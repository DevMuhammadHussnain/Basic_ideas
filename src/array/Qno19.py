# Qno.19
# Input 5 numbers, store in array (list), and print reverse by loop.
# Difficult words:
# - array: collection of items (in Python usually list)
# - reverse: opposite order

arr = []
for i in range(5):
    arr.append(float(input(f"Enter number {i + 1}: ")))

print("Reverse order:")
for i in range(len(arr) - 1, -1, -1):
    print(arr[i])
