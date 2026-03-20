import numpy as np

# ============================================================
# HANDLING MISSING & INVALID VALUES IN NUMPY
# ============================================================
# Missing / invalid values commonly appear in real-world data
# Examples:
# NaN  → Not a Number (missing data)
# inf  → Infinity (divide by zero)
# -inf → Negative infinity

# ------------------------------------------------------------
# 1. Creating array with missing & infinite values
# ------------------------------------------------------------

a = np.array([10, np.nan, 20, np.inf, -np.inf, 30])
print(a)

# ------------------------------------------------------------
# 2. isnan() – Detect NaN values
# ------------------------------------------------------------

# Returns True where value is NaN
nan_mask = np.isnan(a)
print(nan_mask)
# Output: [False  True False False False False]

# Extract non-NaN values
print(a[~nan_mask])

# ------------------------------------------------------------
# 3. isinf() – Detect infinite values
# ------------------------------------------------------------

inf_mask = np.isinf(a)
print(inf_mask)
# Output: [False False False  True  True False]

# ------------------------------------------------------------
# 4. Checking both NaN and Inf
# ------------------------------------------------------------

invalid_mask = np.isnan(a) | np.isinf(a)
print(invalid_mask)

# ------------------------------------------------------------
# 5. Replacing NaN and Inf using nan_to_num()
# ------------------------------------------------------------

# nan_to_num() replaces:
# NaN  → 0 (default)
# inf  → very large number
# -inf → very small number

cleaned = np.nan_to_num(a)
print(cleaned)

# Custom replacement
custom_cleaned = np.nan_to_num(
    a,
    nan=0,
    posinf=9999,
    neginf=-9999
)
print(custom_cleaned)

# ------------------------------------------------------------
# 6. Replacing values manually (using masking)
# ------------------------------------------------------------

b = a.copy()

# Replace NaN with mean of valid values
mean_value = np.nanmean(b)
b[np.isnan(b)] = mean_value
print(b)

# Replace infinity with max valid value
max_value = np.nanmax(b[np.isfinite(b)])
b[np.isinf(b)] = max_value
print(b)

# ------------------------------------------------------------
# 7. Removing missing values
# ------------------------------------------------------------

# Remove NaN & Inf values
clean_array = a[np.isfinite(a)]
print(clean_array)

# ------------------------------------------------------------
# 8. Real-world example: Sensor data
# ------------------------------------------------------------

sensor_data = np.array([25.5, 26.0, np.nan, 27.2, np.inf])

# Replace NaN with average temperature
sensor_data[np.isnan(sensor_data)] = np.nanmean(sensor_data)

# Replace Inf with max safe value
sensor_data[np.isinf(sensor_data)] = np.nanmax(sensor_data)

print(sensor_data)

# ------------------------------------------------------------
# 9. Exam / Interview Key Points
# ------------------------------------------------------------

# isnan() → detects missing values
# isinf() → detects infinite values
# nan_to_num() → replaces NaN & Inf
# isfinite() → valid numbers only
# Use masking for custom replacement
