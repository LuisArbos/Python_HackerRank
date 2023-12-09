"""
Re.start() & Re.end()

start() & end()
These expressions return the indices of the start and end of the substring matched by the group.

Code

>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0

Task
You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Input Format

The first line contains the string S.
The second line contains the string k.

"""
#Python 3:
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S, k = input(), re.compile(input())
start_index, end_index = -1, -1

while 1:
    result = k.search(S, start_index+1)
    if result:
        start_index = result.start()
        end_index = result.end()-1
        print((start_index, end_index))
    else:
        if start_index < 0:
            print((start_index, end_index))
        break


    