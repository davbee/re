import re

# Sample text
text = "I have a quick qwerty brown fox and a lazy dog."

# Regex pattern with negative lookahead
pattern = r"q(?!u)."

# Find all matches
matches = re.findall(pattern, text)

print("Matches:", matches)
