# Qno.24 (Return section duplicate in source text)
# Return sum and average of two numbers.
# Difficult words:
# - average: sum divided by count

def sum_and_average(a, b):
    total = a + b
    avg = total / 2
    return total, avg

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

s, a = sum_and_average(x, y)
print("Sum:", s)
print("Average:", a)
