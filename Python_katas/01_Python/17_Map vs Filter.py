"""
MAP & FILTER – COMPLETE PYTHON GUIDE
------------------------------------
This file contains:

1. map() explanation + examples
2. filter() explanation + examples
3. Normal functions + lambda functions
4. Docstrings included for all custom functions
"""


# -------------------------------
# 1. MAP() FUNCTION
# -------------------------------

def square(x):
    """Returns the square of a number."""
    return x * x

numbers = [1, 2, 3, 4]

# Using map() with a normal function
mapped_result_1 = list(map(square, numbers))
print("map with normal function:", mapped_result_1)


# Using map() with lambda
mapped_result_2 = list(map(lambda n: n * 2, numbers))
print("map with lambda (x2):", mapped_result_2)



# -------------------------------
# 2. FILTER() FUNCTION
# -------------------------------

def is_even(x):
    """Checks if a number is even. Returns True/False."""
    return x % 2 == 0

values = [1, 2, 3, 4, 5, 6]

# Using filter() with normal function
filtered_result_1 = list(filter(is_even, values))
print("filter even numbers:", filtered_result_1)


# Using filter() with lambda
filtered_result_2 = list(filter(lambda x: x > 25, [10, 25, 30, 45, 50]))
print("filter numbers > 25:", filtered_result_2)



# -------------------------------
# 3. COMBINED EXAMPLE
# -------------------------------

def process_numbers(nums):
    """
    Demonstrates map + filter together.

    Steps:
    1. Filter even numbers
    2. Square each even number
    """
    evens = list(filter(lambda x: x % 2 == 0, nums))
    squares = list(map(lambda x: x * x, evens))
    return squares

example_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("Combined map+filter output:", process_numbers(example_list))
