""" 
String Validators

Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.islanum(), .isalpha(), .isdigit(), .islower(), .isupper()

Task

You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters. 

"""

#Python 3:
if __name__ == '__main__':
    s = input()
    bool1 = False
    bool2 = False
    bool3 = False
    bool4 = False
    bool5 = False
    for i in range(len(s)):
        if s[i].isalnum():
            bool1 = True
        if s[i].isalpha():
            bool2 = True
        if s[i].isdigit():
            bool3 = True
        if s[i].islower():
            bool4 = True
        if s[i].isupper():
            bool5 = True
    print(bool1)
    print(bool2)
    print(bool3)
    print(bool4)
    print(bool5)
