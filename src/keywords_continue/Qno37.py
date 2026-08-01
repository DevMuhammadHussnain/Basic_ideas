# Qno.37
# Loop through list of names and skip names that start with 'A'.
# Difficult words:
# - skip: ignore and move forward

names = ["Ali", "Ahmed", "Sara", "Usman", "Areeba", "Zain"]

for name in names:
    if name.startswith("A"):
        continue
    print(name)
