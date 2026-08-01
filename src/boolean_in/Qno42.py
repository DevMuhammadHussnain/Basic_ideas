# Qno.42
# Username/password checker using and.
# Difficult words:
# - validate: check if correct

correct_username = "admin"
correct_password = "1234"

u = input("Enter username: ")
p = input("Enter password: ")

if u == correct_username and p == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")
