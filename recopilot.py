import re

# 11111111
# Sample text
text: str = (
    "John Rolph (1793-1870) was a physician, lawyer, and political "
    "figure. He immigrated to Upper Canada in 1813 and practised law and "
    "medicine concurrently. In 1824, Rolph was elected to the Parliament "
    "of Upper Canada. He was elected as an alderman to Toronto's "
    "first city council but resigned after his council colleagues"
    " did not select him as the city's mayor."
)

# Regex pattern to find the word 'Rolph'
sentence_pattern: str = r"[^.!?;]*Rolph[^.!?;]*[.!?;]"

# Find all sentences containing the pattern
matches: list[str] = re.findall(sentence_pattern, text)

for match in matches:
    print(match.strip())
