"""
A specific state uses license plates that are 7 characters long and must adhere to the following rules:
The first character must be a capital letter (A-Z).
The last character must be a digit (0-9).
The plate must contain at least two vowels ($\text{A, E, I, O, U}$).
"""

import random
import string
def LicensePlateChecker(licensePlate):
    if len(licensePlate) != 7:
        return False
    else:
        capital_letter = string.ascii_uppercase
        digits = string.digits
        vowels=['A','E','I','O','U']
        chars = []
        if (licensePlate[0] in capital_letter) and (licensePlate[-1] in digits):
            for char in licensePlate:
                if char in vowels:
                    chars.append(char)
        else:
            chars=[0]
        if len(chars)>=2:
            return True
        else:
            return False

print(LicensePlateChecker('BEI4UD4'))

