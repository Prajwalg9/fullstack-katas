"""
============================================
        PYTHON MATH MODULE – EXPLAINED
============================================

The `math` module in Python provides mathematical
functions that are fast and precise because they
use C-level implementations.

Why use math module?
- For accurate mathematical calculations
- For functions not available in basic Python
- For handling trigonometry, logarithms,
  constants, power, rounding, etc.

--------------------------------------------
IMPORTANT CONSTANTS
--------------------------------------------
1. math.pi        → 3.141592653589793
2. math.e         → 2.718281828459045
3. math.tau       → 6.283185307179586 (2π)
4. math.inf       → Infinity
5. math.nan       → Not a Number

--------------------------------------------
COMMONLY USED FUNCTIONS
--------------------------------------------

1. **Square Root**
   math.sqrt(x)

2. **Power**
   math.pow(a, b)     # a^b

3. **Absolute Value**
   math.fabs(x)

4. **Factorial**
   math.factorial(n)

5. **Ceil & Floor**
   math.ceil(x)       # goes UP
   math.floor(x)      # goes DOWN

6. **Trigonometry**
   math.sin(x)
   math.cos(x)
   math.tan(x)
   (x should be in radians)

   convert degrees → radians:
   math.radians(degree_value)

7. **Logarithms**
   math.log(x)           # natural log (base e)
   math.log10(x)         # base 10
   math.log2(x)          # base 2

8. **GCD & LCM**
   math.gcd(a, b)
   math.lcm(a, b)

--------------------------------------------
"""

import math

print("\n=========== CONSTANTS ===========")
print("PI:", math.pi)
print("E:", math.e)
print("TAU:", math.tau)

print("\n=========== BASIC FUNCTIONS ===========")
print("Square root of 25:", math.sqrt(25))
print("2 to the power 5:", math.pow(2, 5))
print("Absolute value of -7.9:", math.fabs(-7.9))

print("\n=========== CEIL & FLOOR ===========")
print("math.ceil(4.1):", math.ceil(4.1))
print("math.floor(4.9):", math.floor(4.9))

print("\n=========== FACTORIAL ===========")
print("Factorial of 6:", math.factorial(6))

print("\n=========== TRIGONOMETRY ===========")
degree = 45
radian_value = math.radians(degree)
print(f"Sin({degree}°):", math.sin(radian_value))
print(f"Cos({degree}°):", math.cos(radian_value))
print(f"Tan({degree}°):", math.tan(radian_value))

print("\n=========== LOGARITHMS ===========")
print("Natural log of 10:", math.log(10))
print("Base-10 log of 1000:", math.log10(1000))
print("Base-2 log of 16:", math.log2(16))

print("\n=========== GCD & LCM ===========")
print("GCD of 48 and 18:", math.gcd(48, 18))
print("LCM of 4 and 6:", math.lcm(4, 6))

print("\n=========== SPECIAL VALUES ===========")
print("Infinity example:", math.inf)
print("NaN example:", math.nan)
