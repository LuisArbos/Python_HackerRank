""" 
Check Strict Superset

You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.
Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset. 

Example

Set ([1,3,4]) is a strict superset of set ([1,3]).
Set ([1,3,4]) is not a strict superset of set ([1,3,4]).
Set ([1,3,4]) is not a strict superset of set ([1,3,5]). 

Input Format

The first line contains the space separated elements of set A.
The second line contains integer n, the number of other sets.
The next n lines contains the space separated elements of the other sets. 

"""

#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
set_A = set(map(int, input().split()))
n = int(input())
final_result = False
prev_result = True
for i in range(n):
    temp_set = set(map(int, input().split()))
    if len(set_A) != len(temp_set):
        if len(set_A.intersection(temp_set)) == len(temp_set):
            if prev_result:
                final_result = True
        else:
            final_result = False
            break
            
print(final_result)

