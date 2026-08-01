# Qno.14
# Check if input number is in Fibonacci sequence or not.
# Difficult words:
# - Fibonacci sequence: series where each number is sum of previous two
# - sequence: ordered list of numbers

num = int(input("Enter a number: "))

if num < 0:
    print("Negative numbers are not in standard Fibonacci sequence")
else:
    a, b = 0, 1
    found = (num == 0)

    while a <= num:
        if a == num:
            found = True
            break
        a, b = b, a + b

    print("Number is in Fibonacci sequence" if found else "Number is not in Fibonacci sequence")
