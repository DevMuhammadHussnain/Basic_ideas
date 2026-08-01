# Qno.39
# Loop through list of words and skip words with length < 4.
# Difficult words:
# - characters: letters/symbols in text

words = ["cat", "python", "sun", "code", "AI", "learn"]

for w in words:
    if len(w) < 4:
        continue
    print(w)
