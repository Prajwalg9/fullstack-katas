"""
======================
PYTHON DICTIONARIES – COMPLETE GUIDE IN ONE CODE
======================

WHAT ARE DICTIONARIES?
----------------------
A Python dictionary is a built-in data structure used to store data in
key–value pairs.

Example:
    student = {"name": "Prajwal", "age": 20}

FEATURES:
---------
✔ Keys are unique
✔ Values can be of any data type
✔ Fast lookups (because internally dictionaries use hashing)
✔ Mutable (we can modify, add, remove items)
✔ Unordered collections (but Python 3.7+ maintains insertion order)

REAL-LIFE USES:
---------------
1. Storing user profiles
2. Storing configuration settings
3. Counting frequency of elements
4. Representing JSON data
5. Storing items from databases or APIs

BASIC OPERATIONS:
-----------------
• Creating dictionaries
• Accessing values
• Adding key–value pairs
• Updating values
• Removing items
• Looping through keys/values/items
• Checking if a key exists
• Dictionary methods (get, keys, values, items, pop, etc.)

This code demonstrates EVERYTHING above.
"""

# ---------------------------
# 1. CREATING DICTIONARIES
# ---------------------------
student = {
    "name": "Prajwal",
    "age": 20,
    "skills": ["Python", "JavaScript"],
    "is_active": True
}

print("Original Student Dictionary:")
print(student, "\n")

# ---------------------------
# 2. ACCESSING VALUES
# ---------------------------
print("Accessing name:", student["name"])
print("Accessing skills:", student["skills"])

# Using .get() to avoid error if key does not exist
print("Using get():", student.get("course", "Key not found"), "\n")

# ---------------------------
# 3. ADDING NEW ITEMS
# ---------------------------
student["course"] = "Data Science"
student["score"] = 95

print("After Adding New Keys:")
print(student, "\n")

# ---------------------------
# 4. UPDATING EXISTING VALUES
# ---------------------------
student["age"] = 21   # updating age
student["skills"].append("C Language")  # updating inside list

print("After Updating Values:")
print(student, "\n")

# ---------------------------
# 5. REMOVING ITEMS
# ---------------------------
removed_value = student.pop("score")  # removes and returns the value
print("Removed 'score':", removed_value)
print("Dictionary after pop():", student, "\n")

# Removing last inserted item (Python 3.7+)
student.popitem()
print("After popitem():", student, "\n")

# ---------------------------
# 6. LOOPING THROUGH A DICTIONARY
# ---------------------------

print("Looping through keys:")
for key in student:
    print(key)

print("\nLooping through values:")
for value in student.values():
    print(value)

print("\nLooping through key-value pairs:")
for key, value in student.items():
    print(f"{key} -> {value}")
print()

# ---------------------------
# 7. CHECKING IF A KEY EXISTS
# ---------------------------
print("Is 'age' present?", "age" in student)
print("Is 'score' present?", "score" in student, "\n")

# ---------------------------
# 8. REAL-LIFE USE CASE EXAMPLES
# ---------------------------

# Example 1: Word frequency counter
print("Word Frequency Counter Example:")
sentence = "python is awesome and python is powerful"
words = sentence.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency, "\n")

# Example 2: Storing product info (like JSON)
product = {
    "id": 101,
    "name": "Laptop",
    "price": 55000,
    "specs": {
        "brand": "HP",
        "ram": "16GB",
        "storage": "512GB SSD"
    }
}
print("Product Dictionary:", product)
print("Product Brand:", product["specs"]["brand"], "\n")

