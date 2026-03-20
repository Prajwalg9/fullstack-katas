import numpy as np

# ============================================================
# RESHAPING, MANIPULATING & FLATTENING ARRAYS IN NUMPY
# ============================================================

# ------------------------------------------------------------
# 1. RESHAPING ARRAYS
# ------------------------------------------------------------
# Reshaping means changing the structure (shape) of an array
# WITHOUT changing its data.

a = np.arange(12)
print(a)
# Output: [ 0  1  2  3  4  5  6  7  8  9 10 11 ]

# reshape(rows, columns)
b = a.reshape(3, 4)
print(b)
# Output:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Using -1 (NumPy auto-calculates dimension)
c = a.reshape(2, -1)
print(c)
# Output:
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]

# Important rule:
# rows * columns must equal total elements
# Otherwise ValueError occurs

# ------------------------------------------------------------
# 2. MANIPULATING ARRAY SHAPES
# ------------------------------------------------------------

# transpose()
# Swaps rows and columns
print(b.T)
# Output:
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]

# swapaxes()
# Swaps two axes
print(np.swapaxes(b, 0, 1))

# expand_dims()
# Adds a new dimension at specified axis
d = np.expand_dims(a, axis=0)
print(d.shape)    # (1, 12)

# squeeze()
# Removes single-dimensional entries
print(np.squeeze(d).shape) # (12,)

# ------------------------------------------------------------
# 3. FLATTENING ARRAYS
# ------------------------------------------------------------
# Flattening converts multi-dimensional arrays into 1D

# flatten()
# Returns a COPY of the array
flat1 = b.flatten()
print(flat1)
# Output: [ 0  1  2  3  4  5  6  7  8  9 10 11 ]

# ravel()
# Returns a VIEW (shares memory if possible)
flat2 = b.ravel()
print(flat2)

# reshape(-1)
# Another way to flatten
flat3 = b.reshape(-1)
print(flat3)

# ------------------------------------------------------------
# 4. DIFFERENCE: flatten() vs ravel()
# ------------------------------------------------------------

flat2[0] = 999
print(b)
# ravel() changes original array (view)

flat1[1] = 888
print(b)
# flatten() does NOT change original array