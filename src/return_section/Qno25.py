# Qno.25 (Return section duplicate in source text)
# Return sum, average, and multiplication of two numbers.
# Difficult words:
# - multiplication: product of numbers using *

def sum_avg_mul(a, b):
    total = a + b
    avg = total / 2
    mul = a * b
    return total, avg, mul

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

s, a, m = sum_avg_mul(x, y)
print("Sum:", s)
print("Average:", a)
print("Multiplication:", m)
