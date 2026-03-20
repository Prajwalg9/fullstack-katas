import numpy as np

# ============================================================
# VECTORIZATION IN NUMPY
# ============================================================
# Vectorization means performing operations on ENTIRE ARRAYS
# at once instead of using loops.
# NumPy executes vectorized code in optimized C, making it FAST.

# ------------------------------------------------------------
# 1. Basic Vectorized Operations
# ------------------------------------------------------------

a = np.array([1, 2, 3, 4, 5])

# Multiply each element by 2 (NO LOOP)
result = a * 2
print(result)
# Output: [ 2  4  6  8 10 ]

# ------------------------------------------------------------
# 2. Salary Increment (Real-world example)
# ------------------------------------------------------------

salary = np.array([30000, 40000, 50000, 60000])

# 10% hike for all employees
new_salary = salary + salary * 0.10
print(new_salary)

# No for-loop required → vectorized

# ------------------------------------------------------------
# 3. Student Marks Conversion
# ------------------------------------------------------------

marks = np.array([35, 50, 65, 80])

# Add grace marks
updated_marks = marks + 5
print(updated_marks)

# ------------------------------------------------------------
# 4. Electricity Bill Calculation
# ------------------------------------------------------------

units = np.array([120, 200, 150])

rate = 6  # per unit

bill = units * rate
print(bill)

# ------------------------------------------------------------
# 5. Using NumPy Universal Functions (ufuncs)
# ------------------------------------------------------------

data = np.array([1, 4, 9, 16])

print(np.sqrt(data))     # Square root
print(np.log(data))      # Logarithm
print(np.exp(data))      # Exponential

# ------------------------------------------------------------
# 6. Vectorization in 2D Arrays
# ------------------------------------------------------------

sales = np.array([[100, 200, 300],
                  [150, 250, 350]])

# Increase sales by 20%
updated_sales = sales * 1.20
print(updated_sales)

# ------------------------------------------------------------
# 7. Comparison: Loop vs Vectorization
# ------------------------------------------------------------

# LOOP approach (slow)
result_loop = []
for i in sales.flatten():
    result_loop.append(i * 1.20)

# VECTORIZED approach (fast)
result_vector = sales * 1.20

# ------------------------------------------------------------
# 8. Why Vectorization is Important
# ------------------------------------------------------------

# Faster execution
# Less code
# More readable
# Used in ML, Data Analysis, Scientific Computing

# ------------------------------------------------------------
# 9. Exam / Interview Key Points
# ------------------------------------------------------------

# Vectorization avoids explicit loops
# Uses NumPy's optimized C backend
# Works well with broadcasting
