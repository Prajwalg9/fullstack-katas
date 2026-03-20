"""
csv_module_demo.py

Demonstrates Python's csv module:
- csv.reader / csv.writer
- Reading/writing with headers
- csv.DictReader / csv.DictWriter
- Handling special characters
"""

import csv

# =============================
# 1. Writing a simple CSV file
# =============================
data = [
    ['Name', 'Age', 'Job'],
    ['Alice', 30, 'Engineer'],
    ['Bob', 25, 'Data Scientist'],
    ['Charlie', 35, 'Teacher'],
]

with open('people.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write all rows at once

print("1. Created 'people.csv' with sample data.")

# =============================
# 2. Reading CSV using csv.reader
# =============================
with open('people.csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)       # Get the header row
    print("\n2. Header:", header)
    for row in reader:
        print("Row:", row)

# =============================
# 3. Writing CSV with DictWriter (field names as headers)
# =============================
people = [
    {'Name': 'Dana', 'Age': 28, 'Job': 'Designer'},
    {'Name': 'Eli', 'Age': 40, 'Job': 'Manager'}
]
fieldnames = ['Name', 'Age', 'Job']

with open('people_dict.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()          # Write headers
    writer.writerows(people)      # Write data

print("\n3. Created 'people_dict.csv' using DictWriter.")

# =============================
# 4. Reading CSV with DictReader (each row as dict)
# =============================
with open('people_dict.csv', 'r', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("\n4. Rows from 'people_dict.csv' as dicts:")
    for row in reader:
        print(row)

# =============================
# 5. Handling special characters & quoting
# =============================
special_rows = [
    ['Name', 'Comment'],
    ['Frank', 'Loves, commas'],
    ['Grace', 'Quotes " and, commas, are fun!'],
]

with open('special.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerows(special_rows)

print("\n5. Wrote 'special.csv' with quoting for tricky characters.")

# =============================
# 6. Reading CSV with different delimiter
# =============================
semicolon_data = [
    ['A', 'B', 'C'],
    ['1', '2', '3'],
]
with open('semicolons.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(semicolon_data)

with open('semicolons.csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=';')
    print("\n6. semicolons.csv rows:")
    for row in reader:
        print(row)

# =============================
# 7. Appending to a CSV file
# =============================
with open('people.csv', 'a', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Daisy', 22, 'Intern'])

print("\n7. Appended a row to 'people.csv'.")

# =============================
# Summary prompt
# =============================
print("\n--- Summary ---")
print("You now know how to use the csv module to read, write, append, and handle headers and special cases.")

# Practice: Try editing, running, or viewing the created files yourself!
