# Qno.28
# Input 5 numbers and print them in reverse order in a function.
# Difficult words:
# - reverse: opposite direction/order

def input_and_reverse_print():
    nums = []
    for i in range(5):
        nums.append(float(input(f"Enter number {i + 1}: ")))

    print("Reverse order:")
    for i in range(len(nums) - 1, -1, -1):
        print(nums[i])

input_and_reverse_print()
