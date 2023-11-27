""" 
itertools.permutations()

This tool returns successive r length permutations of elements in an iterable.

If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

Example:

>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]

Task

You are given a string S.
Your task is to print all possible permutations of size of the string in lexicographic sorted order.

"""

#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

inp = list(input().split())
final_list = [''.join(i) for i in itertools.permutations(str(inp[0]), int(inp[1]))]
for i in sorted(final_list):
    print(i)


