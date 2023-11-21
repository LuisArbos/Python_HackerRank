""" 
sWAP cASE

You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

"""

#Python 3:

def swap_case(s):
    final_string = ""
    for i in range(len(s)):
        if s[i].upper() == s[i]:
            final_string += s[i].lower()
        else:
            final_string += s[i].upper()
    return final_string

