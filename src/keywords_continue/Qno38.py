# Qno.38
# Loop through list of numbers and skip numbers less than 10.
# Difficult words:
# - less than: smaller than

numbers = [3, 7, 10, 12, 5, 20, 9, 15]

for n in numbers:
    if n < 10:
        continue
    print(n)
