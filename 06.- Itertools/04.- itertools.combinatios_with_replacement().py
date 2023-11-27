""" 
itertools.combinatios_with_replacement()

This tool returns r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Example:

>>> from itertools import combinations_with_replacement
>>> 
>>> print list(combinations_with_replacement('12345',2))
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]


Task

You are given a string S.
Your task is to print all possible size replacement combinations of the string in lexicographic sorted order.

"""

#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
inp = list(input().split())
final_list = []
final_list.extend([''.join(combination) for combination in itertools.combinations_with_replacement(sorted(str(inp[0])), int(inp[1]))])
for j in sorted(final_list, key=lambda x: (len(x), x)):
    print(j)



