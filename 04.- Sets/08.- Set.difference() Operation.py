""" 
Set.difference() Operation

.difference()

The tool .difference() returns a set with all the elements from the set that are not in an iterable.
Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
Set is immutable to the .difference() operation (or the - operation).

Task

Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

"""

#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
int_english = int(input())
english_set= set(map(int, input().split()))
int_french = int(input())
french_set= set(map(int, input().split()))
print(len(english_set.difference(french_set)))


