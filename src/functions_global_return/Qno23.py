# Qno.23
# Functionality of (+, -, *, /) based on user input data.
# Difficult words:
# - functionality: features or operations the code can perform
# - operator: symbol that performs operation (+, -, *, /)

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: division by zero"
        return a / b
    else:
        return "Error: invalid operator"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

print("Result:", calculate(num1, num2, operator))
