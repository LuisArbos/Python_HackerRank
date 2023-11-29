"""
DefaultDict Tutorial

The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
For example:

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i

This prints:

('python', ['awesome', 'language'])
('something-else', ['not relevant'])

In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Input Format

The first line contains integers, n and m separated by a space.
The next lines contains the words belonging to group A.
The next lines contains the words belonging to group B.

"""
#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
n, m = map(int, input().split())
A = collections.defaultdict(list)

for i in range(1, n+1):
    inp = input()
    A[inp].append(i)

for i in range(m):
    inp2 = input()
    if inp2 in A.keys():
        print(*A[inp2])
    else:
        print(-1)
