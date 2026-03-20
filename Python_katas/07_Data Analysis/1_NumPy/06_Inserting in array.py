import numpy as np

# ============================================================
# INSERTING ELEMENTS IN NUMPY ARRAYS
# ============================================================

# IMPORTANT NOTE:
# NumPy arrays are FIXED SIZE.
# Inserting does NOT modify the original array.
# It returns a NEW array.

# ------------------------------------------------------------
# 1. np.insert() – Insert elements at a specific index
# ------------------------------------------------------------

a = np.array([10, 20, 30, 40])

# Insert 99 at index 2
b = np.insert(a, 2, 99)
print(b)
# Output: [10 20 99 30 40]

# Original array remains unchanged
print(a)
# Output: [10 20 30 40]

# ------------------------------------------------------------
# 2. Inserting multiple values
# ------------------------------------------------------------

# Insert multiple values at index 1
c = np.insert(a, 1, [100, 200])
print(c)
# Output: [10 100 200 20 30 40]



# ------------------------------------------------------------
# 3. Inserting in 2D arrays (axis)
# ------------------------------------------------------------

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Insert a new ROW (axis = 0)
row_insert = np.insert(arr, 1, [7, 8, 9], axis=0)
print(row_insert)
# Output:
# [[1 2 3]
#  [7 8 9]
#  [4 5 6]]

# Insert a new COLUMN (axis = 1)
col_insert = np.insert(arr, 1, [10, 11], axis=1)
print(col_insert)
# Output:
# [[ 1 10  2  3]
#  [ 4 11  5  6]]