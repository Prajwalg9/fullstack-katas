import numpy as np

# ============================================================
# CONCATENATION IN NUMPY
# ============================================================
# Concatenation means JOINING two or more arrays
# along a SPECIFIED AXIS.
# Uses: np.concatenate()

# ------------------------------------------------------------
# 1. Concatenation of 1D arrays
# ------------------------------------------------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.concatenate((a, b))
print(result)
# Output: [1 2 3 4 5 6]

# ------------------------------------------------------------
# 2. Concatenation of 2D arrays
# ------------------------------------------------------------

x = np.array([[1, 2, 3],
              [4, 5, 6]])

y = np.array([[7, 8, 9],
              [10, 11, 12]])

# axis = 0 → row-wise (vertical)
row_concat = np.concatenate((x, y), axis=0)
print(row_concat)

# axis = 1 → column-wise (horizontal)
col_concat = np.concatenate((x, y), axis=1)
print(col_concat)

# ------------------------------------------------------------
# 3. Shape rules (VERY IMPORTANT)
# ------------------------------------------------------------

# axis = 0 → number of columns must match
# axis = 1 → number of rows must match

# ------------------------------------------------------------
# 4. Exam / Interview Key Points
# ------------------------------------------------------------

# np.concatenate() is flexible
# axis must be specified for 2D arrays
# Returns a NEW array
