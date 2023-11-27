""" 
Maximize It!

You are given a function f(X) = X^2. You are also given K lists. The i^th list consists of Ni elements.

You have to pick one element from each list so that the value from the equation below is maximized:

S = (f(X1) + f(X2) + ... + f(Xk))%M

Xi denotes the element picked from the i^th list. Find the maximized value Smax obtained.

% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains 2 space separated integers K and M.
The next K lines each contains an integer Ni, denoting the number of elements in the i^th list, followed by Ni space separated integers denoting the elements in the list. 

"""

#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

k, m = map(int, input().split())
li = []

for i in range(k):
    li.append(set(map(lambda x: int(x)**2 % m, input().split()[1:])))

print(max(set(sum(x) % m for x in itertools.product(*li))))



