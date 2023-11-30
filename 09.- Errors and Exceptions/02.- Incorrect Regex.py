"""
Incorrect Regex

You are given a string S.
Your task is to find out whether S is a valid regex or not.

Input Format

The first line contains integer T, the number of test cases.
The next T lines contains the string S.

Output Format

Print "True" or "False" for each test case without quotes.

"""
#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T = int(input())
for _ in range(T):
    S = input()
    try:
        re.compile(S)
        print("True")
    except re.error:
        print("False")
        
"""I had to submit this code in pypy 3, because the current version of Python 3 the page is using, supports both test inputs. That means instead of printing True and False, is printing True and True. They need to update the challenge for current Python 3 version. """