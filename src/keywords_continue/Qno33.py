# Qno.33
# Input a string and print string with vowels skipped using continue.
# Difficult words:
# - vowels: a, e, i, o, u

text = input("Enter a string: ")
vowels = "aeiouAEIOU"

result = ""
for ch in text:
    if ch in vowels:
        continue
    result += ch

print("Without vowels:", result)
