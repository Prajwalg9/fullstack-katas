import numpy as np

# -------------------------------
# Reshaping Arrays
# -------------------------------

# Create an array from 0 to 5
a = np.arange(6)
print(a)              # Output: [0 1 2 3 4 5]

# reshape()
# Changes the shape of the array without changing data
# (rows, columns)
b = a.reshape(2, 3)
print(b)
# Output:
# [[0 1 2]
#  [3 4 5]]

# -------------------------------
# flatten() and ravel()
# -------------------------------

# flatten()
# Returns a 1D COPY of the array
c = b.flatten()
print(c)              # Output: [0 1 2 3 4 5]

# ravel()
# Returns a 1D VIEW of the array (shares memory)
d = b.ravel()
print(d)              # Output: [0 1 2 3 4 5]

# -------------------------------
# Mathematical Operations (Vectorization)
# -------------------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
print(a + b)          # Output: [5 7 9]

# Element-wise Substraction
print(a - b)          # Output: [-3 -3 -3]

# Element-wise multiplication
print(a * b)          # Output: [ 4 10 18 ]

# Element-wise Devision
print(a / b)          # Output: [0.25 0.4  0.5 ]

# Element-wise Exponential
print(a ** b)          # Output: [  1  32 729]

# Element-wise Modulus
print(a % b)          # Output: [1 2 3]

# Square root of each element
print(np.sqrt(a))     # Output: [1.         1.41421356 1.73205081]

# Sum of all elements
print(np.sum(a))      # Output: 6

# Mean (average) of elements
print(np.mean(a))     # Output: 2.0
