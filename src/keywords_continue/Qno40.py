# Qno.40
# Loop through list of numbers and skip numbers greater than 50.
# Difficult words:
# - greater than: bigger than

numbers = [10, 25, 51, 60, 40, 5, 100, 49]

for n in numbers:
    if n > 50:
        continue
    print(n)
