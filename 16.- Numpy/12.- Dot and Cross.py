"""
Dot and Cross

dot

The dot tool returns the dot product of two arrays.

import numpy
A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])
print numpy.dot(A, B)       #Output : 11

cross

The cross tool returns the cross product of two arrays.

import numpy
A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])
print numpy.cross(A, B)     #Output : -2

Task

You are given two arrays A and B. Both have dimensions of NxM.
Your task is to compute their matrix product.

Input Format

The first line contains the integer N.
The next N lines contains N space separated integers of array A.
The following N lines contains N space separated integers of array B.
"""

#Python 3:
import numpy
N = int(input())
li, li2 = [], []
for _ in range(N):
    li.append(list(map(int, input().split())))
arr_A = numpy.array(li)
for _ in range(N):
    li2.append(list(map(int, input().split())))
arr_B = numpy.array(li2)
print(numpy.dot(arr_A, arr_B))
