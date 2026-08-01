# Qno.30
# Return input length, print it, then multiply length outside function.
# Difficult words:
# - length: number of characters
# - multiply: repeated addition using *

def get_length(text):
    return len(text)

user_input = input("Enter text: ")
length_value = get_length(user_input)

print("Length:", length_value)
print("Length x 2:", length_value * 2)
