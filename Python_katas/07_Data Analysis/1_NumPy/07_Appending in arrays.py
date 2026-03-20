import numpy as np

# ============================================================
# APPENDING ELEMENTS IN NUMPY ARRAYS
# ============================================================

# ------------------------------------------------------------
# 1. np.append() – Append at the end of array
# ------------------------------------------------------------

a = np.array([10, 20, 30])

# Append single element
b = np.append(a, 40)
print(b)
# Output: [10 20 30 40]

# Original array remains unchanged
print(a)
# Output: [10 20 30]

# ------------------------------------------------------------
# 2. Appending multiple elements
# ------------------------------------------------------------

c = np.append(a, [50, 60])
print(c)
# Output: [10 20 30 50 60]

# ------------------------------------------------------------
# 3. Appending in 2D arrays (axis)
# ------------------------------------------------------------

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Append a new ROW (axis = 0)
row_append = np.append(arr, [[7, 8, 9]], axis=0)
print(row_append)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Append a new COLUMN (axis = 1)
col_append = np.append(arr, [[10], [11]], axis=1)
print(col_append)
# Output:
# [[ 1  2  3 10]
#  [ 4  5  6 11]]