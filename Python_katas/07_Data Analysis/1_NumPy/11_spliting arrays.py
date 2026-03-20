import numpy as np

# ============================================================
# SPLITTING ARRAYS IN NUMPY
# ============================================================
# Splitting means dividing an array into multiple sub-arrays.
# Functions: split(), hsplit(), vsplit(), array_split()

# ------------------------------------------------------------
# 1. np.split() – Equal splitting
# ------------------------------------------------------------

a = np.array([10, 20, 30, 40, 50, 60])

# Split into 3 equal parts
b = np.split(a, 3)
print(b)
# Output:
# [array([10, 20]),
#  array([30, 40]),
#  array([50, 60])]

# NOTE:
# Total elements MUST be divisible by number of splits

# ------------------------------------------------------------
# 2. Splitting using indices
# ------------------------------------------------------------

# Split at index positions 2 and 4
c = np.split(a, [2, 4])
print(c)
# Output:
# [array([10, 20]),
#  array([30, 40]),
#  array([50, 60])]

# ------------------------------------------------------------
# 3. np.array_split() – Unequal splitting
# ------------------------------------------------------------

d = np.array_split(a, 4)
print(d)
# Output:
# Unequal-sized sub-arrays allowed

# ------------------------------------------------------------
# 4. Splitting 2D arrays
# ------------------------------------------------------------

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

# Horizontal split (columns)
h = np.hsplit(arr, 2)
print(h)

# Vertical split (rows)
v = np.vsplit(arr, 2)
print(v)

# ------------------------------------------------------------
# 5. Exam / Interview Key Points
# ------------------------------------------------------------

# split() → equal parts only
# array_split() → unequal parts allowed
# hsplit() → column-wise split
# vsplit() → row-wise split
