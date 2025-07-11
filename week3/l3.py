import re

words = ["apple", "banana", "orange", "grape", "umbrella"]

vowel_caps = list(map(lambda w: re.sub(r'^[aeiou](\w+)', w.upper(), w), words))
print(vowel_caps)