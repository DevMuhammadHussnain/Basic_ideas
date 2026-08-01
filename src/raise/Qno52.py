"""
Qno.52: Raise an exception if a username or password is empty.

Difficult words:
- exception: an error event in program flow.
- empty: having no characters/data.
"""

def validate_credentials(username, password):
    if username == "" or password == "":
        raise Exception("Username or password cannot be empty.")
    return True


u = input("Enter username: ")
p = input("Enter password: ")

try:
    if validate_credentials(u, p):
        print("Credentials look good")
except Exception as e:
    print(e)
