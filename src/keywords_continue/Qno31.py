# Qno.31 (mapped from Basic Level keywords starting page 5)
# Input and continue inputs till user inputs 'l'.
# Difficult words:
# - continue: skip to next loop step
# - till: until

while True:
    value = input("Enter something (enter 'l' to stop): ")
    if value == "l":
        break
    print("You entered:", value)
