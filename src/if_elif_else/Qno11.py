# Qno.11
# Check if input number is palindrome or not.
# Difficult words:
# - palindrome: same when read forward and backward

num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
