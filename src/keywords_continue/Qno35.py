# Qno.35
# Loop through passwords, skip weak ones (len < 6 or only letters).
# Difficult words:
# - weak password: easy to guess/insecure
# - len: length of text

passwords = ["abc", "hello12", "python", "A1b2c3", "secret"]

for pwd in passwords:
    if len(pwd) < 6 or pwd.isalpha():
        continue
    print("Strong enough:", pwd)
