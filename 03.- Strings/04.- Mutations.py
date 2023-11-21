""" 
Mutations

We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it. 

Task
Read a given string, change the character at a given index and then print the modified string.

Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

    - string string: the string to change
    - int position: the index to insert the character at
    - string character: the character to insert

Returns

    - string: the altered string

"""

#Python 3:

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string
