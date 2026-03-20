import numpy as np

# ============================================================
# BROADCASTING IN NUMPY
# ============================================================
# Broadcasting allows NumPy to perform operations on arrays
# of DIFFERENT SHAPES without using loops.
# It automatically expands the smaller array.

# ------------------------------------------------------------
# 1. Simple Broadcasting (Scalar + Array)
# ------------------------------------------------------------

prices = np.array([100, 200, 300, 400])

# Add GST (18%) to all prices
final_prices = prices + prices * 0.18
print(final_prices)
# Real-world: Applying tax to multiple products at once

# ------------------------------------------------------------
# 2. Salary Increment (Real-world example)
# ------------------------------------------------------------

salary = np.array([30000, 40000, 50000])

# 10% hike for everyone
new_salary = salary + salary * 0.10
print(new_salary)

# Broadcasting applies 10% to each employee automatically

# ------------------------------------------------------------
# 3. Student Marks Adjustment
# ------------------------------------------------------------

marks = np.array([65, 70, 80, 90])

# Grace marks +5 to all students
updated_marks = marks + 5
print(updated_marks)

# ------------------------------------------------------------
# 4. Broadcasting in 2D Arrays
# ------------------------------------------------------------

sales = np.array([[100, 200, 300],
                  [150, 250, 350]])

# Monthly bonus added to each column (product-wise)
bonus = np.array([10, 20, 30])

total_sales = sales + bonus
print(total_sales)

# bonus shape (3,) → broadcast to (2,3)

# ------------------------------------------------------------
# 5. Electricity Bill Calculation (Real-world)
# ------------------------------------------------------------

units = np.array([[120, 150, 180],
                  [200, 220, 250]])

rate = np.array([5, 6, 7])

bill = units * rate
print(bill)

# Each column has different rate per unit

# ------------------------------------------------------------
# 6. Broadcasting Rules (IMPORTANT)
# ------------------------------------------------------------

# Two dimensions are compatible if:
# 1) They are equal
# OR
# 2) One of them is 1

# Example:
# (2,3) + (3,) → VALID
# (2,3) + (2,) → INVALID

# ------------------------------------------------------------
# 7. Broadcasting vs Loops (Performance)
# ------------------------------------------------------------

# Broadcasting is:
# Faster
# Cleaner
# More readable
# Avoids loops

# BAD (loop approach):
result = []
for i in prices:
    result.append(i + i * 0.18)

# GOOD (broadcasting):
result = prices + prices * 0.18

# ------------------------------------------------------------
# 8. Interview / Exam Key Points
# ------------------------------------------------------------

# Broadcasting avoids explicit loops
# Smaller array is stretched automatically
# Used heavily in data analysis & ML
