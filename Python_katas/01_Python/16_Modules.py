"""
PYTHON MODULES – COMPLETE GUIDE IN ONE FILE
-------------------------------------------
This single file explains:

1. What a module is
2. How to import modules
3. Built-in module examples (math, random, datetime, os, sys)
4. Creating a user-defined module inside the SAME file
5. Using __name__ == "__main__"
"""

# ----------------------------------------------------
# 1. BUILT-IN MODULE EXAMPLES
# ----------------------------------------------------

import math
import random
import datetime
import os
import sys

print("math.sqrt(25):", math.sqrt(25))
print("math.pi:", math.pi)

print("random number (1-10):", random.randint(1, 10))

now = datetime.datetime.now()
print("current date & time:", now)

print("current working directory:", os.getcwd())

print("python executable:", sys.executable)


# ----------------------------------------------------
# 2. USER-DEFINED MODULE (inside the same file)
# ----------------------------------------------------
# In real Python projects, this would be in another file like:
#   mymodule.py
#
# But since you want everything IN ONE FILE,
# we will simulate a module using a class as a container.


class mymodule:
    """Simulating a user-defined module in the same file."""

    def greet(name):
        """Returns a greeting."""
        return f"Hello, {name}!"

    def add(a, b):
        """Adds two numbers."""
        return a + b


# Using our user-defined module (simulated)
print("mymodule.greet:", mymodule.greet("Prajwal"))
print("mymodule.add:", mymodule.add(10, 20))


# ----------------------------------------------------
# 3. DIFFERENT IMPORT METHODS (shown in one file)
# ----------------------------------------------------

# Method 1: import module
import math as m
print("alias import -> m.sqrt(36):", m.sqrt(36))

# Method 2: from module import function
from math import factorial
print("from math import factorial:", factorial(5))


# ----------------------------------------------------
# 4. __name__ == '__main__' EXPLANATION
# ----------------------------------------------------
# Normally used to prevent code from running when imported.
# Here it will always run because this file is not imported.

def demo():
    print("Executed only when file runs directly.")

if __name__ == "__main__":
    demo()
