import re

# text: str = r"https://regexr.com/66vrt"
# pattern: str = r"(?:https?|ftp):\/\/([^\/\r\n]+)(\/[^\r\n]*)?"

# match = re.search(pattern, text)
# print(match)

import re

# Sample URL
url = "https://www.example.com/path/to/page?name=example&lang=en"

# Regular expression pattern to match the URL components
pattern = (
    r"^(https?://)?(www\.)?([a-zA-Z0-9.-]+)(/[a-zA-Z0-9./-]*)?(\?[a-zA-Z0-9=&]*)?$"
)

# Using re.match to find the components
match = re.match(pattern, url)

if match:
    protocol = match.group(1) or "http"
    subdomain = match.group(2) or ""
    domain = match.group(3)
    path = match.group(4) or ""
    query = match.group(5) or ""

    print(f"Protocol: {protocol}")
    print(f"Subdomain: {subdomain}")
    print(f"Domain: {domain}")
    print(f"Path: {path}")
    print(f"Query: {query}")
else:
    print("Invalid URL")
