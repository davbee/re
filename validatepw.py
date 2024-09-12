import re

# 11111111
# Sample text
text: str = "Ostsee6174$"
pattern: str = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"

matches: list[str] = re.findall(pattern, text)

if matches:
    print("Welcome to Ostsee.")
else:
    print("Invalid password.  Please enter password again.")
