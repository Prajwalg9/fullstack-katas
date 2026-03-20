import re

# findall() returns all non-overlapping matches of pattern in string, as a list of strings
text = "There are 2 apples and 5 oranges"
matches = re.findall(r'\d+', text)  # \d+ matches one or more digits
print("Numbers found:", matches)  # Output: Numbers found: ['2', '5']



# search() scans through string, looking for the first location where the pattern matches
text = "welcome to Regex!"
result = re.search(r"Regex", text)  # Searches for "Regex" anywhere in the string
if result:
    print("Found at position:", result.start())  # Output: Found at position: 11




# match() checks for a match only at the beginning of the string
text = "Hello world"
result = re.match(r"Hello", text)  # Looks for "Hello" at the start of the string
if result:
    print("Match found:", result.group())  # Output: Match found: Hello