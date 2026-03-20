import re

# Character class example: Find email addresses using character classes and special sequences
text = "My email: john@example.com"
result = re.findall(r'\w+@\w+\.\w+', text)  # \w+ matches word chars (letters, numbers, underscore), @ and . are literal, so finds simple emails
print("Emails found:", result)  # Output: Emails found: ['john@example.com']



# ^ matches the start, $ the end of a string
text = "Start here. End there."
start = re.search(r'^Start', text)  # Checks if string starts with "Start"
end = re.search(r'there\.$', text)  # Checks if string ends with "there."
print("Start anchor found:", bool(start))  # Output: Start anchor found: True
print("End anchor found:", bool(end))      # Output: End anchor found: True



# Parentheses () form groups for capturing parts of the match
text = "Jan 21, Feb 12"
result = re.findall(r'(\w+) (\d+)', text)  # Captures month and day number as tuples
print("Month and day:", result)  # Output: Month and day: [('Jan', '21'), ('Feb', '12')]