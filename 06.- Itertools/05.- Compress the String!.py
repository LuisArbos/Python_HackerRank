""" 
itertools.product()

In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools. To read more about this function, Check this out .

You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X, c) in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string S. 

Example:

Input:
1222311

Output:
(1, 1) (3, 2) (1, 3) (2, 1)

Explanation

First, the character
occurs only once. It is replaced by . Then the character occurs three times, and it is replaced by

and so on.

Also, note the single space within each compression and between the compressions. 
"""

#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
inp = input()
for c, X in itertools.groupby(inp):
    counter = len(list(X))
    print('({}, {})'.format(counter, c), end=" ")

