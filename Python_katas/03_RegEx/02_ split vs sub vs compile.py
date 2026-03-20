import re

# sub() replaces matches with a specified string
text = "Python 2, Python 3"
result = re.sub(r'\d', 'X', text)  # Replaces all digits with 'X'
print("Substituted text:", result)  # Output: Substituted text: Python X, Python X


# compile() compiles a regular expression into a regex object for repeated use
pattern = re.compile(r'\w+')  # \w+ matches sequences of alphanumeric characters
matches = pattern.findall("Regex makes things easy!")
print("Words:", matches)  # Output: Words: ['Regex', 'makes', 'things', 'easy']



# split() splits a string by the matches of the pattern, returns a list
text = "apple,banana;grape orange"
result = re.split(r'[;, ]+', text)  # Splits at any comma, semicolon, or whitespace
print("Split items:", result)  # Output: Split items: ['apple', 'banana', 'grape', 'orange']