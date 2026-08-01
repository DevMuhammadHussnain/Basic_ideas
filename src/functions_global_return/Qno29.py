# Qno.29
# Return 'a' if user input is 'a', else print 'b'.
# Difficult words:
# - return: send value back from function

def check_value(value):
    if value == "a":
        return "a"
    return None

user_input = input("Enter a value: ")
result = check_value(user_input)

if result == "a":
    print(result)
else:
    print("b")
