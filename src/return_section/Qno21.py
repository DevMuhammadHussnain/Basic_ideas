# Qno.21 (Return section duplicate in source text)
# Return username and password as user input.
# Difficult words:
# - credentials: login data (username/password)

def get_credentials():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

u, p = get_credentials()
print("Username:", u)
print("Password:", p)
