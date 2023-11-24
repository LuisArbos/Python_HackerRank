""" 
Set.union() Operation

.union()

The .union() operator returns the union of a set and the set of elements in an iterable.
Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
Set is immutable to the .union() operation (or | operation).

Task

The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

"""

#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
int_english = int(input())
english_set= set(map(int, input().split()))
int_french = int(input())
french_set= set(map(int, input().split()))

print(len(english_set | french_set))
