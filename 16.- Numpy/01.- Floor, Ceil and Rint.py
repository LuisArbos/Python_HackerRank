"""
Floor, Ceil and Rint

floor
The tool floor returns the floor of the input element-wise.
The floor of x is the largest integer i where i<=x.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

ceil
The tool ceil returns the ceiling of the input element-wise.
The ceiling of x is the smallest integer i where i>=x.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

rint
The rint tool rounds to the nearest integer of input element-wise.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

Task
You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A. 
"""

#Python 3:
import numpy
numpy.set_printoptions(legacy='1.13')

arr = list(map(float, input().split()))
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
