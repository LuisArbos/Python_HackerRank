"""
Array Mathematics

Basic mathematical functions operate element-wise on arrays. They are available both as operator overloads and as functions in the NumPy module.

import numpy

a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print a + b                     #[  6.   8.  10.  12.]
print numpy.add(a, b)           #[  6.   8.  10.  12.]

print a - b                     #[-4. -4. -4. -4.]
print numpy.subtract(a, b)      #[-4. -4. -4. -4.]

print a * b                     #[  5.  12.  21.  32.]
print numpy.multiply(a, b)      #[  5.  12.  21.  32.]

print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]

print a % b                     #[ 1.  2.  3.  4.]
print numpy.mod(a, b)           #[ 1.  2.  3.  4.]

print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]

Task

You are given two integer arrays, A and B of dimensions NxM.
Your task is to perform the following operations:
   - Add (A+B)
   - Subtract (A-B)
   - Multiply (A*B)
   - Integer Division (A/B)
   - Mod (A%B)
   - Power (A**B)

Input Format

The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array B. 

"""

#Python 3:
import numpy

N, M = list(map(int, input().split()))
li_A = []
li_B = []
for _ in range(N):
    li_A.append(list(map(int, input().split())))
for _ in range(N):
    li_B.append(list(map(int, input().split())))
arr_A = numpy.array(li_A, dtype=int)
arr_B = numpy.array(li_B, dtype=int)
print(numpy.add(arr_A, arr_B))
print(numpy.subtract(arr_A, arr_B))
print(numpy.multiply(arr_A, arr_B))
print(numpy.floor_divide(arr_A, arr_B))
print(numpy.mod(arr_A, arr_B))
print(numpy.power(arr_A, arr_B))
