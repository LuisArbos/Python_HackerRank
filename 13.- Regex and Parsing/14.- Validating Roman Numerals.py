"""
Validating Roman Numerals

You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.

Input Format

A single line of input containing a string of Roman characters.

Constraints

The number will be between 1 and 3999 (both included).
"""

#Python 3:
regex_pattern = r"^(M){0,3}(CM)?(D)?(CD)?(C){0,3}(XC)?(L)?(XL)?(X){0,3}(IX)?(V)?(IV)?(I){0,3}$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
