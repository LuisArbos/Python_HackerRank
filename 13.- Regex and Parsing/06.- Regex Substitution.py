"""
Regex Substitution

The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
The method is called for all matches and can be used to modify strings in different ways.
The re.sub() method returns the modified string as an output.

Transformation of Strings

Code

import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")

Output

1 4 9 16 25 36 49 64 81

Task

You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:

&& → and
|| → or

Both && and || should have a space " " on both sides. 

"""
#Python 3:
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    S = input()
    S = re.sub(r"(?<=\s)([&&])\1(?=\s)", "and", S)
    S = re.sub(r"(?<=\s)([||])\1(?=\s)", "or", S)
    print(S)


    