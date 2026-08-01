# Qno.12
# Check if input number is an Armstrong number or not.
# Difficult words:
# - Armstrong number: number equal to sum of its own digits raised to power of count of digits

num = int(input("Enter a number: "))
num_str = str(num)
power = len(num_str)
armstrong_sum = sum(int(digit) ** power for digit in num_str)

if num == armstrong_sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
