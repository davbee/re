import re

# 11111111
# Sample text
text: str = "John Rolph (1793-1870) was a physician, lawyer, and political "\
    "figure. He immigrated to Upper Canada in 1813 and practised law and "\
    "medicine concurrently. In 1824, Rolph was elected to the Parliament "\
    "of Upper Canada. He was elected as an alderman to Toronto's "\
    "first city council but resigned after his council colleagues"\
    " did not select him as the city's mayor."

# Regex pattern to find the word 'Canada'
# sentence_pattern: str = r"([^.!?]*?Canada[^.!?]*[.?!;] )"
sentence_pattern: str = r"[^.!?]*Canada[^.!?]*[.!?]"
# Find all sentences containing the pattern
matches: list[str] = re.findall(sentence_pattern, text)

for match in matches:
    print(match.strip())

# 22222222
# Sample text2
text2: str = "localhost_sm_smaall_1.sql"

# Regex pattern to find the word per pattern
sentence_pattern2: str = r"(?<=[_]).*(?=[.])"

matches2: list[str] = re.findall(sentence_pattern2, text2)

for match in matches2:
    print(match.strip())

# 33333333
# regex pattern before the regex pattern
foreregex: str = r"^.+?(?=Rolph)"
# find the portion of the sentence before the regex pattern
forematch = re.search(foreregex, text)
print(forematch.group())

# 44444444
# regex pattern before the regex pattern
postregex: str = r"(?<=Rolph).+"
# find the portion of the sentence after the regex pattern
postmatch = re.search(postregex, text)
print(postmatch.group())
