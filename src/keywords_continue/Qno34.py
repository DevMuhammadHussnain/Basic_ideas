# Qno.34
# Loop 1 to 100 and skip numbers divisible by both 3 and 5.
# Difficult words:
# - divisible: can be divided without remainder

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        continue
    print(i)
