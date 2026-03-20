"""
exception_handling_explained.py

This script demonstrates Python exception handling:
- try, except, else, finally
- Catching specific and multiple exceptions
- The raise statement
- File handling with exceptions
"""

# 1. Basic try-except: catch any error and keep the program running
try:
    print(10 / 0)
except Exception as e:  # catches any exception
    print("Caught an error:", e)

# 2. Catch a specific exception (recommended!)
try:
    x = int("hello")
except ValueError:
    print("That was not a number!")  # only runs if ValueError happens

# 3. Catch multiple exception types
try:
    f = open("no_such_file.txt", "r")
    value = 5 / 0
except FileNotFoundError:
    print("The file was not found.")
except ZeroDivisionError:
    print("Tried to divide by zero.")
# You can add as many except blocks as needed

# 4. Use else: only runs if no exceptions happen in the try
try:
    y = 10 / 2
except ZeroDivisionError:
    print("Divide by zero!")
else:
    print("Division worked, result =", y)

# 5. Use finally: always runs, even if an error or not (good for cleanup)
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("List index error.")
finally:
    print("Cleanup or always-run code goes here.")

# 6. File handling with exceptions (best practice)
try:
    with open("maybe.txt", "r") as f:
        content = f.read()
        print("File content:", content)
except FileNotFoundError:
    print("File does not exist. Please check your path.")  # [5][8]

# 7. Using raise to trigger your own exception deliberately
def only_positive(num):
    if num < 0:
        raise ValueError("Number must be positive!")  # [7]
    return num

try:
    only_positive(-5)
except ValueError as err:
    print("Custom error:", err)

# 8. Catch-all except (not best practice, but you may see it)
try:
    print(100 / 0)
except:    # no exception type given: catches everything
    print("Generic error happened.")

# 9. Nested try-except and exception chaining
try:
    try:
        x = 1 / 0
    except ZeroDivisionError as zde:
        print("First error:", zde)
        raise RuntimeError("Something else went wrong") from zde
except RuntimeError as re:
    print("Chained error:", re)

# --- End of tutorial ---

"""
Summary:
- Use try, except to *catch* errors so your program doesn't crash.
- Catch *specific* exceptions for best practice.
- else runs if no errors, finally always runs.
- Use 'raise' to signal your own exceptions.
- Handle file errors gracefully.
- Practice: modify one block at a time to see new results!
"""
