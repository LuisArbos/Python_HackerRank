""" 
itertools.combinations()

This tool returns the

length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Example: 

>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]



Task

You are given a string S.
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

"""

#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
inp = list(input().split())
final_list = []
for i in range(1, int(inp[1])+1):
    final_list.extend([''.join(combination) for combination in itertools.combinations(sorted(str(inp[0])), i)])
for j in sorted(final_list, key=lambda x: (len(x), x)):
    print(j)

