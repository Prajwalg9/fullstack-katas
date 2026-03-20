"""
PYTHON OS MODULE – COMPLETE GUIDE IN ONE FILE
---------------------------------------------
This file explains and demonstrates everything using the os module:

1. Get current working directory
2. Change directory
3. List files & folders
4. Create folders (single & nested)
5. Remove folders (single & nested)
6. Rename files/folders
7. Check path/file/folder existence
8. Joining paths safely
9. File information (size, time)
10. Environment variables
11. Running system commands
12. Absolute paths
13. Splitting paths & extensions
"""

import os


# ----------------------------------------------------
# 1. GET CURRENT WORKING DIRECTORY
# ----------------------------------------------------
print("Current directory:", os.getcwd())


# ----------------------------------------------------
# 2. CHANGE DIRECTORY
# (NOTE: Change the path below if needed)
# ----------------------------------------------------
# Example (commented to avoid errors):
# os.chdir("C:/Users")
# print("Changed directory:", os.getcwd())


# ----------------------------------------------------
# 3. LIST FILES & FOLDERS
# ----------------------------------------------------
print("List of files & folders:", os.listdir("."))


# ----------------------------------------------------
# 4. CREATE FOLDERS
# ----------------------------------------------------
# Create a single folder
# os.mkdir("myfolder")

# Create nested folders
# os.makedirs("data/project/logs", exist_ok=True)


# ----------------------------------------------------
# 5. REMOVE FOLDERS
# ----------------------------------------------------
# Remove single empty folder
# os.rmdir("myfolder")

# Remove nested directories
# os.removedirs("data/project/logs")


# ----------------------------------------------------
# 6. RENAME FILES OR FOLDERS
# ----------------------------------------------------
# Example:
# os.rename("old.txt", "new.txt")


# ----------------------------------------------------
# 7. CHECK PATH / FILE / FOLDER EXISTENCE
# ----------------------------------------------------
print("Does sample.txt exist?", os.path.exists("sample.txt"))
print("Is it a file?", os.path.isfile("sample.txt"))
print("Is it a folder?", os.path.isdir("sample.txt"))


# ----------------------------------------------------
# 8. JOIN PATHS SAFELY
# ----------------------------------------------------
safe_path = os.path.join("C:/Users", "Prajwal", "Desktop", "file.txt")
print("Joined safe path:", safe_path)


# ----------------------------------------------------
# 9. GET FILE INFORMATION
# ----------------------------------------------------
# Example (only works if file exists):
# info = os.stat("sample.txt")
# print("File size:", info.st_size)
# print("Last modified:", info.st_mtime)


# ----------------------------------------------------
# 10. ENVIRONMENT VARIABLES
# ----------------------------------------------------
print("User Home:", os.environ.get("USERPROFILE", "Not found"))

# Set custom environment variable
os.environ["MY_VAR"] = "Prajwal Test"
print("Custom env var MY_VAR:", os.environ["MY_VAR"])


# ----------------------------------------------------
# 11. RUNNING SYSTEM COMMANDS
# ----------------------------------------------------
# Works on Windows:
print("\nRunning 'dir' command:")
os.system("dir")   # lists files


# ----------------------------------------------------
# 12. GET ABSOLUTE PATH
# ----------------------------------------------------
abs_path = os.path.abspath("sample.txt")
print("Absolute path of sample.txt:", abs_path)


# ----------------------------------------------------
# 13. SPLITTING PATHS
# ----------------------------------------------------
path = "C:/Users/Prajwal/Desktop/image.png"

print("Split path:", os.path.split(path))        # (directory, file)
print("Split extension:", os.path.splitext(path))# (filename, extension)
