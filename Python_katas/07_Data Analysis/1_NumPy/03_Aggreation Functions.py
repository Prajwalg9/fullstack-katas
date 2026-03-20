import numpy as np

# Aggregation functions
# Used to perform calculations on the entire array
# or along a specific axis (row-wise / column-wise)

a = np.array([[1, 2, 3],
              [4, 5, 6]])

# sum()
# Returns sum of elements
print(np.sum(a))            # Output: 21

# mean()
# Returns average of elements
print(np.mean(a))           # Output: 3.5

# min()
# Returns minimum value
print(np.min(a))            # Output: 1

# max()
# Returns maximum value
print(np.max(a))            # Output: 6

# std()
# Returns standard deviation
print(np.std(a))            # Output: 1.707825...

# var()
# Returns variance
print(np.var(a))            # Output: 2.916666...

# -------------------------------
# Using axis
# -------------------------------

# axis = 0 → column-wise operation
print(np.sum(a, axis=0))    # Output: [5 7 9]

# axis = 1 → row-wise operation
print(np.sum(a, axis=1))    # Output: [ 6 15 ]

# -------------------------------
# Other common aggregation functions
# -------------------------------

print(np.median(a))         # Middle value
print(np.percentile(a, 50))# 50th percentile (same as median)
