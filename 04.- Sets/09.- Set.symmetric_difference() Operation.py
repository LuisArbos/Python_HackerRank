""" 
Set.symmetric_difference() Operation

.symmetric_difference()

The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
The set is immutable to the .symmetric_difference() operation (or ^ operation).

Task

Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

"""

#Python 3:
# Enter your code here. Read input from STDIN. Print output to STDOUT
int_english = int(input())
english_set= set(map(int, input().split()))
int_french = int(input())
french_set= set(map(int, input().split()))
print(len(english_set.symmetric_difference(french_set)))

