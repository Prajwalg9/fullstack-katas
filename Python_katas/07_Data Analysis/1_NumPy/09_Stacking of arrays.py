import numpy as np

# ============================================================
# STACKING IN NUMPY
# ============================================================
# Stacking is a SPECIAL CASE of concatenation
# Used to combine arrays vertically or horizontally
# Functions: vstack(), hstack(), column_stack(), dstack()

# ------------------------------------------------------------
# 1. Vertical Stacking (vstack)
# ------------------------------------------------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

v = np.vstack((a, b))
print(v)
# Output:
# [[1 2 3]
#  [4 5 6]]

# ------------------------------------------------------------
# 2. Horizontal Stacking (hstack)
# ------------------------------------------------------------

h = np.hstack((a, b))
print(h)
# Output: [1 2 3 4 5 6]

# ------------------------------------------------------------
# 3. Column Stack
# ------------------------------------------------------------

c = np.column_stack((a, b))
print(c)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

# ------------------------------------------------------------
# 4. Depth Stack (dstack)
# ------------------------------------------------------------

d = np.dstack((a, b))
print(d)
# Output shape: (1, 3, 2)

# ------------------------------------------------------------
# 5. Exam / Interview Key Points
# ------------------------------------------------------------

# vstack() → stacks row-wise
# hstack() → stacks column-wise for 2D, end-to-end for 1D
# column_stack() → converts 1D arrays into columns
# dstack() → stacks along third axis
