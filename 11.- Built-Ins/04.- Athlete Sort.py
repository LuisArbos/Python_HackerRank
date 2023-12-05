"""
Athlete Sort

You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). You are required to sort the K^th data based on the th attribute and print the final resulting table.

Note that is indexed from 0 to M-1, where M is the number of attributes.

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

Input Format

The first line contains N and M separated by a space.
The next N lines each contain M elements.
The last line contains K. 

Output Format

Print the N lines of the sorted table. Each line should contain the space separated elements.

"""
#Python 3:

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

#My code:
    for i in sorted(arr, key=lambda item: item[k]):
        print(*i)



    