""" 
Find a string

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.


"""

#Python 3:

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        count += string.count(sub_string, i, i+len(sub_string))
    return count
