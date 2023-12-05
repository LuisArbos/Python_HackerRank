"""
Zipped!

zip([iterable, ...])

This function returns a list of tuples. The
th tuple contains the

th element from each of the argument sequences or iterables.

If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence. 

Example:

>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
>>> 
>>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
>>> 
>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C]
>>> 
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]

Task

The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.

Average scopre = Sum of scores obtained in all subject by student / Total number of subjects

"""
#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
students = []
for _ in range(X):
    students.append(list(map(float, input().split())))

for i in zip(*students):
    print(round(sum(i)/X, 1))

    