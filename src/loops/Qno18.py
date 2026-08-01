# Qno.18
# Input 5 numbers and print them using loop.
# Difficult words:
# - input: data entered by user

numbers = []
for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("You entered:")
for num in numbers:
    print(num)
