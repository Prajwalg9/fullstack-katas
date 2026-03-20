#String functions

s1="Hello World! I am a python developer."
print(s1)

#to find length of string:
print(len(s1))

# Indexing (positive and negative)
print("\nIndexing examples:")
print(s1[0])   # First character
print(s1[1])   # Second character
print(s1[4])   # Fifth character
print(s1[-1])  # Last character

# Slicing: string[start:end:step]
print("\nSlicing examples:")
print(s1[2:7:1])   # llo W
print(s1[::2])     # Every 2nd character from start
print(s1[1::2])    # Every 2nd character from index 1
print(s1[::-2])    # Every 2nd character in reverse order
print(s1[4:9:2])   # oWr

#f-String
name="prajwal"
age=19
lang="python"
hours=4
print(f"{name} is {age} years old. And studies {lang} {hours} hours a day.")

#string repetition operator
name="Hello "
print(name*3)

#membership operator : There is "in" & "not in" keyword which tells if something exists in something
s1="Python is Fun!"
print("Python" in s1)
print("java" not in s1)
print("Fun" not in s1)

#Comparison of strings
s1="Python"
print("Python " == s1)
print("python" == s1)
s1="      Python                    "
#strip is used to remove extra starting and ending spaces
print("python" == s1.strip())

#replacing sub-string from string
s1="Python is high level interpreted object oriented mulipurpose language"
print(s1)
print(s1.replace("Python", "Java"))


#counting substrings from string
s1="we are learning python! Python is fun."
print(s1.count("Python"))

#changing Cases in python
s1="Python3.13 is the Programming Language."
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.capitalize())

#stars with & ends with
s1="we are learning python! Python is fun."
print(s1.startswith("we"))
print(s1.startswith("are"))
print(s1.endswith("fun."))
print(s1.endswith("."))