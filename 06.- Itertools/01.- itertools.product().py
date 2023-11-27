""" 
itertools.product()

This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B). 

Example: 

>>> from itertools import product
>>>
>>> print list(product([1,2,3],repeat = 2))
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

Task

You are given a two lists A and B. Your task is to compute their cartesian product AXB.

"""

#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

final_list = list(itertools.product(a_list, b_list))
print(*final_list, sep=" ")


