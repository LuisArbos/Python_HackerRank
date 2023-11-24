""" 
Set Mutations

We have seen the applications of union, intersection, difference and symmetric difference operations, but these operations do not make any changes or mutations to the set.

We can use the following operations to create mutations to a set:

.update() or |=
Update the set by adding elements from an iterable/another set.

.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

TASK
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.

"""

#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
len_A = int(input())
A_set= set(map(int, input().split()))
other_sets = int(input())

for i in range(other_sets):
    operation = list(input().split())
    operation_set = set(map(int, input().split()))
    
    match operation[0]:
        case "intersection_update":
            A_set.intersection_update(operation_set)
        case "update":
            A_set.update(operation_set)
        case "symmetric_difference_update":
            A_set.symmetric_difference_update(operation_set)
        case "difference_update":
            A_set.difference_update(operation_set)
        case other:
            print("Wrong command")
    
print(sum(A_set))

