"""
file_handling_explained.py

Covers:
- open()
- write()
- writelines()
- read()
- readline()
- readlines()
- seek()
- tell()
- close()
- with open(...) as (context manager)
- Modes: "r", "w", "a", "x", "b", "+"
"""

# 1. open(): Open a file (returns a file object)
#    First arg: filename. Second arg: mode, like "r" for read, "w" for write, etc.
f = open("demo.txt", "w", encoding="utf-8")  # "w" means write. If file exists, it's overwritten.

# 2. write(): Write a string to the file
f.write("First line!\n")
f.write("Second line!\n")
# Returns number of characters written.

# 3. writelines(): Write a list of strings to a file (no line breaks added)
lines = ["Third line!\n", "Fourth line!\n"]
f.writelines(lines)

# 4. tell(): Get current file position (in bytes)
pos = f.tell()
print("File position after writing:", pos)

# 5. close(): Always close files to save changes and free resources
f.close()

# 6. read(): Read entire file as a single string
f = open("demo.txt", "r", encoding="utf-8")
content = f.read()
print("Using read():\n", content)
f.close()

# 7. readline(): Reads ONE line (including the '\n'), moves to next line each call
f = open("demo.txt", "r", encoding="utf-8")
print("Using readline():")
print(f.readline().strip())   # First line
print(f.readline().strip())   # Second line
f.close()

# 8. readlines(): Read all lines into a LIST of strings
f = open("demo.txt", "r", encoding="utf-8")
lines = f.readlines()
print("Using readlines():", lines)
f.close()

# 9. seek(): Move to a particular byte position in the file
#    This is useful for re-reading or skipping around.
f = open("demo.txt", "r", encoding="utf-8")
f.seek(0)        # Go back to start
print("First 10 bytes:", f.read(10))
f.close()

# 10. 'with' statement (context manager): auto-closes files
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write("Appended line!\n")  # In 'a' (append) mode, new data goes at the end

# 11. Reading file line-by-line (saves memory if file is large)
print("Line-by-line reading:")
with open("demo.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# 12. Modes (quick guide)
# "r"   = read, "w" = write (overwrite!), "a" = append, "x" = create new file (error if exists)
# Add "b" for binary (e.g., "rb", "wb")
# Add "+" for read & write ("r+", "w+")
# Example: Write binary data
with open("demo.bin", "wb") as f:
    f.write(b'\x41\x42')   # Writes bytes A (65), B (66)

# 13. Always handle exceptions (not required, but good practice)
try:
    f = open("notfound.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("notfound.txt does not exist")
finally:
    if 'f' in locals() and not f.closed:
        f.close()
