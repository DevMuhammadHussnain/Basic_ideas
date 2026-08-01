# Qno.27
# Save password in data by global within function.
# Difficult words:
# - global: variable that can be used outside function

password_data = ""

def save_password():
    global password_data
    password_data = input("Enter password: ")

save_password()
print("Password saved in global variable.")
