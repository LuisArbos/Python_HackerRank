""" 
String Split and Join

In Python, a string can be split on a delimiter. example: a.split(" "). It also can be joined like a = "-".join(a).

Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

    - string line: a string of space-separated words

Returns

    - string: the resulting string


"""

#Python 3:

def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line
