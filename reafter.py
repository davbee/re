import re

text:str = "This is a sample text. Pattern: Here is the sentence you want. Another sentence."

pattern: str = r"Pattern:\s*(.*?)(?:\.|$)"
pattern: str = r"(?<=Pattern: )(.*?)(?:\.|$)"

match = re.search(pattern, text)
print(match)
if match:
    print(match.group())
