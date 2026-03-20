import numpy as np

# ============================================================
# DELETING ELEMENTS IN NUMPY ARRAYS
# ============================================================
# IMPORTANT:
# NumPy arrays are FIXED in size.
# Deleting does NOT modify the original array.
# It always returns a NEW array.

# ------------------------------------------------------------
# 1. np.delete() – Delete elements by index
# ------------------------------------------------------------

a = np.array([10, 20, 30, 40, 50])

# Delete element at index 2
b = np.delete(a, 2)
print(b)
# Output: [10 20 40 50]

# Original array remains unchanged
print(a)
# Output: [10 20 30 40 50]

# ------------------------------------------------------------
# 2. Deleting multiple elements
# ------------------------------------------------------------

# Delete elements at indices 1 and 3
c = np.delete(a, [1, 3])
print(c)
# Output: [10 30 50]

# ------------------------------------------------------------
# 3. Deleting elements from 2D arrays
# ------------------------------------------------------------

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Delete a ROW (axis = 0)
row_deleted = np.delete(arr, 1, axis=0)
print(row_deleted)
# Output:
# [[1 2 3]
#  [7 8 9]]

# Delete a COLUMN (axis = 1)
col_deleted = np.delete(arr, 0, axis=1)
print(col_deleted)
# Output:
# [[2 3]
#  [5 6]
#  [8 9]]

# ------------------------------------------------------------
# 4. Deleting using condition (Boolean masking)
# ------------------------------------------------------------

x = np.array([5, 10, 15, 20, 25])

# Remove elements greater than 15
result = x[x <= 15]
print(result)
# Output: [ 5 10 15 ]

# ------------------------------------------------------------
# 5. Difference: delete() vs Boolean masking
# ------------------------------------------------------------

# np.delete() → delete by index
# Boolean masking → delete by condition

# ------------------------------------------------------------
# 6. Exam / Interview Key Points
# ------------------------------------------------------------

# np.delete() returns a NEW array
# axis=0 → delete row
# axis=1 → delete column
# Boolean masking is preferred for conditions
