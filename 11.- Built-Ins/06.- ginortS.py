"""
ginortS

You are given a string S. S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:

    - All sorted lowercase letters are ahead of uppercase letters.
    - All sorted uppercase letters are ahead of digits.
    - All sorted odd digits are ahead of sorted even digits.

Input Format

A single line of input contains the string S.

"""
#Python 3:
# Enter your code here. Read input from STDIN. Print output to STDOUT
print(*sorted(str(input()), key=lambda x: (x.isdigit(), x.isupper(), x.islower(), x in "02468", x)), sep="")


    