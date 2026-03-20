import numpy as np

# --------------------------------
# 1. Basic Indexing
# --------------------------------

a = np.array([10, 20, 30, 40, 50])

# Access single element (0-based index)
print(a[0])        # Output: 10
print(a[-1])       # Output: 50 (last element)

# 2D indexing
b = np.array([[1, 2, 3],
              [4, 5, 6]])

print(b[0, 1])     # Output: 2 (row 0, column 1)

# --------------------------------
# 2. Slicing
# --------------------------------

# Syntax: start : stop : step

print(a[1:4])      # Output: [20 30 40]
print(a[:3])       # Output: [10 20 30]
print(a[::2])      # Output: [10 30 50]

# 2D slicing
print(b[:, 1])     # Output: [2 5]  (all rows, column 1)
print(b[1, :])     # Output: [4 5 6] (row 1, all columns)

# --------------------------------
# 3. Fancy Indexing
# --------------------------------

# Using list/array of indices
c = np.array([100, 200, 300, 400, 500])

print(c[[0, 2, 4]])   # Output: [100 300 500]

# Fancy indexing in 2D
print(b[[0, 1], [1, 2]])
# Output: [2 6]

# --------------------------------
# 4. Boolean Masking
# --------------------------------

d = np.array([5, 10, 15, 20, 25])

# Condition returns boolean array
mask = d > 15
print(mask)           # Output: [False False False True True]

# Apply condition
print(d[d > 15])      # Output: [20 25]

# --------------------------------
# 5. Combining Conditions
# --------------------------------

# Use & (and), | (or), ~ (not)
print(d[(d > 10) & (d < 25)])   # Output: [15 20]

# --------------------------------
# 6. Modify values using masking
# --------------------------------

d[d < 15] = 0
print(d)              # Output: [ 0  0 15 20 25 ]
