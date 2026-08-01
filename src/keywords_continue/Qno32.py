# Qno.32
# Loop 1 to 20 and print only odd numbers using continue.
# Difficult words:
# - odd: not divisible by 2

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)
