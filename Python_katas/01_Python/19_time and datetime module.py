"""
PYTHON TIME & DATETIME MODULE – COMPLETE GUIDE IN ONE FILE
----------------------------------------------------------
This file contains:

TIME MODULE:
1. time.time()
2. time.sleep()
3. time.ctime()
4. time.localtime()
5. time.strftime()
6. Stopwatch example

DATETIME MODULE:
1. datetime.datetime.now()
2. datetime.date()
3. datetime.time()
4. datetime.datetime()
5. Formatting dates (strftime)
6. Parsing string to date (strptime)
7. Timedelta (date difference)
8. Adding/Subtracting days
"""

import time
import datetime


# ----------------------------------------------------
# 1. TIME MODULE
# ----------------------------------------------------

print("\n=== TIME MODULE ===")

# 1. time.time() – returns seconds since 1970
print("Current timestamp:", time.time())

# 2. time.sleep() – pauses program
print("Waiting for 1 second...")
time.sleep(1)
print("Done!")

# 3. time.ctime() – human readable time
print("Current readable time:", time.ctime())

# 4. time.localtime() – full structure
lt = time.localtime()
print("Local time structure:", lt)

# 5. time.strftime() – format date/time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted time:", formatted_time)

# 6. Stopwatch example
print("\nStopwatch demo starting...")
start = time.time()
time.sleep(0.5)
end = time.time()
print("Time difference:", end - start, "seconds")



# ----------------------------------------------------
# 2. DATETIME MODULE
# ----------------------------------------------------

print("\n=== DATETIME MODULE ===")

# 1. Current date & time
now = datetime.datetime.now()
print("Now:", now)

# 2. Date object
d = datetime.date(2025, 11, 18)
print("Custom date:", d)

# 3. Time object
t = datetime.time(15, 30, 45)
print("Custom time:", t)

# 4. Complete datetime object
dt = datetime.datetime(2025, 11, 18, 15, 30, 45)
print("Custom datetime:", dt)

# 5. Formatting datetime (strftime)
formatted_dt = now.strftime("%d-%m-%Y | %I:%M %p")
print("Formatted datetime:", formatted_dt)

# 6. Parsing string to datetime (strptime)
date_string = "2025-11-18 14:25:30"
parsed = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed)

# 7. Timedelta – difference between dates
date1 = datetime.date(2025, 1, 1)
date2 = datetime.date(2025, 11, 18)
difference = date2 - date1
print("Difference between dates:", difference.days, "days")

# 8. Adding/Subtracting days
today = datetime.date.today()
after_7_days = today + datetime.timedelta(days=7)
before_7_days = today - datetime.timedelta(days=7)
print("Today:", today)
print("After 7 days:", after_7_days)
print("Before 7 days:", before_7_days)
