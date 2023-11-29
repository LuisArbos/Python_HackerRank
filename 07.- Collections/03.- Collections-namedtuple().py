"""
Collections-namedtuple()

Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

Example

Code 01

>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11

Task

Dr. John Wesley has a spreadsheet containing a list of student's ID, marks, class and name.

Your task is to help Dr. Wesley calculate the average marks of the students.

Average = Sum of all marks / Total Students

Input Format

The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the marks, IDs, name and class, under their respective column names.

"""
#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
res = 0
N = int(input())
Data = collections.namedtuple('Students', (list(input().split())))
for _ in range(N):
    res += int(Data(*list(input().split())).MARKS)

print(res/N)
