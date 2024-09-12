import re


# MMetacharacters
# Metacharacters are characters with a special meaning:

# Character	Description	Example	Try it
# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"planet$"
# *	Zero or more occurrences	"he.*o"
# +	One or more occurrences	"he.+o"
# ?	Zero or one occurrences	"he.?o"
# {}	Exactly the specified number of occurrences	"he.{2}o"
# |	Either or	"falls|stays"
# ()	Capture and group
# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

# Character	Description	Example	Try it
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"

# r"ain\b"

# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"

# r"ain\B"

# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# \D	Returns a match where the string DOES NOT contain digits	"\D"
# \s	Returns a match where the string contains a white space character	"\s"
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
# Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:

# Set	Description	Try it
# [arn]	Returns a match where one of the specified characters (a, r, or n) is present
# [a-n]	Returns a match for any lower case character, alphabetically between a and n
# [^arn]	Returns a match for any character EXCEPT a, r, and n
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]	Returns a match for any digit between 0 and 9
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string


# Search the string to see if it starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x[0])
if x:
    print("YES! We have a match!")
else:
    print("No match")

# Print a list of all matches:
x = re.findall("ai", txt)
print(x)

# Search for the first white-space character in the string:
x = re.search(r"\s", txt)
print("The first white-space character is located in position:", x.start())

# Split at each white-space character:
x = re.split(r"\s", txt)
print(x)

# Split the string only at the first occurrence:
x = re.split(r"\s", txt, 1)
print(x)

# Replace every white-space character with the number 9:
x = re.sub(r"\s", "9", txt)
print(x)

# Replace the first 2 occurrences:
x = re.sub(r"\s", "9", txt, 2)
print(x)

# Do a search that will return a Match Object:
x = re.search("ai", txt)
print(x)

# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":

x = re.search(r"\bS\w+", txt)
print(x.span())

# Print the string passed into the function:
x = re.search(r"\bS\w+", txt)

print("xxxx")
print(x.string)

# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":
x = re.search(r"\bT\w+", txt)
print(x.group())
print(x[0])

pattern = r"(\d{3})-(\d{2})-(\d{4})"
text = "My number are 123-45-6789 and 408-96-0640"
match = re.search(pattern, text)
print(match[0])

if match:
    print(match.group(1))  # Output: 123
    print(match.group(2))  # Output: 45
    print(match.group(3))  # Output: 6789
    # print(match.group(4))  # Output: 6789

pattern = r"(?P<area_code>\d{3})-(?P<exchange>\d{2})-(?P<number>\d{4})"
match = re.search(pattern, text)
if match:
    print(match.group("area_code"))  # Output: 123
    print(match.group("exchange"))  # Output: 45
    print(match.group("number"))  # Output: 6789

pattern = r"(\d{3}-\d{2}-\d{4})"
text = "Numbers: 123-45-6789, 987-65-4321"
matches = re.findall(pattern, text)
print(matches)  # Output: [('123', '45', '6789'), ('987', '65', '4321')]
