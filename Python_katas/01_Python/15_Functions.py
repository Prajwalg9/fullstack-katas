"""
PYTHON FUNCTIONS – COMPLETE GUIDE WITH DOCSTRINGS
-------------------------------------------------
This file covers:

1. Basic function
2. Function with parameters
3. Function with return value
4. Default parameters
5. Multiple returns
6. Keyword arguments
7. *args
8. **kwargs
9. Lambda functions
10. Recursion
11. Docstrings for every function
"""


# 1. BASIC FUNCTION
def greet():
    """Prints a welcome message."""
    print("Hello! welcome to Python.")

greet()


# 2. FUNCTION WITH PARAMETERS
def add(a, b):
    """
    Adds two numbers and prints the result.

    Parameters:
        a (int/float): First number
        b (int/float): Second number
    """
    print("Addition:", a + b)

add(5, 10)


# 3. FUNCTION WITH RETURN VALUE
def multiply(a, b):
    """
    Returns the multiplication of two numbers.

    Returns:
        int/float: product of a and b
    """
    return a * b

result = multiply(4, 6)
print("Multiplication:", result)


# 4. DEFAULT PARAMETERS
def welcome(name="Guest"):
    """
    Greets a user by name. If no name provided, uses 'Guest'.
    """
    print("Hello", name)

welcome()
welcome("Prajwal")


# 5. MULTIPLE RETURNS
def calculate(a, b):
    """
    Returns both addition and subtraction of two numbers.

    Returns:
        tuple: (addition, subtraction)
    """
    return a + b, a - b

x, y = calculate(10, 4)
print("Add:", x, "Subtract:", y)


# 6. KEYWORD ARGUMENTS
def intro(name, age):
    """
    Prints user information using keyword arguments.
    """
    print("Name:", name, "| Age:", age)

intro(age=20, name="Riya")


# 7. *ARGS
def total_sum(*numbers):
    """
    Accepts unlimited numbers and prints the total sum.

    Parameters:
        *numbers: List of numeric values
    """
    print("Total sum is:", sum(numbers))

total_sum(1, 2, 3, 4, 5)


# 8. **KWARGS
def person_info(**details):
    """
    Accepts unlimited keyword arguments and prints them.

    Parameters:
        **details: key=value pairs
    """
    print("Person details:", details)

person_info(name="Amit", age=21, city="Mumbai")


# 9. LAMBDA FUNCTION (with doc comment)
square = lambda x: x * x  # Small anonymous function to return square
print("Square:", square(5))


# 10. RECURSION
def factorial(n):
    """
    Returns factorial using recursion.

    Parameters:
        n (int): number

    Returns:
        int: factorial of n
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
