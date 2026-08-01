# Qno.15
# Check if input number is strong number or not.
# Difficult words:
# - strong number: number equal to sum of factorials of its digits
# - factorial: product of all positive integers up to that number

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
sum_fact = sum(factorial(int(digit)) for digit in str(num))

if num == sum_fact:
    print("Strong number")
else:
    print("Not a strong number")
