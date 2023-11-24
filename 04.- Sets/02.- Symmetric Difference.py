""" 
Symmetric Difference

Objective
Today, we're learning about a new data type: sets.

Concept

If the inputs are given on one line separated by a character (the delimiter), use split() to get the separate values in the form of a list. The delimiter is space (ascii 32) by default. To specify that comma is the delimiter, use string.split(','). For this challenge, and in general on HackerRank, space will be the delimiter.

Usage:

>> a = raw_input()
5 4 3 2
>> lis = a.split()
>> print (lis)
['5', '4', '3', '2']

If the list values are all integer types, use the map() method to convert all the strings to integers.

>> newlis = list(map(int, lis))
>> print (newlis)
[5, 4, 3, 2]

Sets are an unordered collection of unique values. A single set contains values of any immutable data type. 

Task
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

"""

#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
M_in = (input().split(" "))
N = int(input())
N_in = (input().split(" "))
M_set= set()
N_set = set()
final_set = set()

for i in range(len(M_in)):
    M_set.add(M_in[i])
    final_set.add(M_in[i])
for i in range(len(N_in)):
    N_set.add(N_in[i])
    final_set.add(N_in[i])
"""Now final_set contains all the values from M and N, just need to discard the ones that are in both and then reorder all in ascending order. As the sets are unordered we will convert them into a sorted list to print them"""

for values in M_set.intersection(N_set):
    final_set.discard(values)
    
sorted_nums = sorted(map(int, final_set))
for num in sorted_nums:
    print(num)
