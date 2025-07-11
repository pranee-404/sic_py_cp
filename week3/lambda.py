#lambda and regex
import re
data = ["abc123", "hello2024", "no digits", "zip007"]

#extracting digits from a string
digits = list(map(lambda s: re.findall(r'[a-z]+', s), data))
print(digits)

#replacing/substituting
replace = list(map(lambda s: re.sub(r'\D+', '', s), data))
print(replace)