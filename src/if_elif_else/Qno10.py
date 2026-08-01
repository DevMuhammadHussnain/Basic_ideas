# Qno.10
# Check if input number is prime or not.
# Difficult words:
# - prime: number greater than 1 with only two factors (1 and itself)
# - factor: number that divides another number completely

num = int(input("Enter a number: "))

if num <= 1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    print("Prime" if is_prime else "Not prime")
