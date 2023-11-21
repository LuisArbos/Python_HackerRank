""" 
Merge the Tools!

Consider the following:

    - A string, s, of length n, where s =c0c1...cn-1.
    - An integer, k, where is a factor of n.

We can split s into n/k substrings where each subtring, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

    - The characters in ui are a subsequence of the characters in ti.
    - Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not include the character in string ui.

Given s and k, print n/k lines where each line i denotes string ui. 

"""

#Python 3:

def merge_the_tools(string, k):
    # your code goes here
    start = 0
    end = k
    t = []
    if k != 1:
        for i in range(k):
            t.append(string[start:end])
            start += k
            end += k
        for j in range(len(t)):
            print("".join(dict.fromkeys(t[j])))
    else:
        for i in range(len(string)):
            print(string[i])
    
    

