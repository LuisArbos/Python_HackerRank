"""
Word Order

You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Input Format

The first line contains the integer, n.
The next n lines each contain a word. 

Output Format

Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

"""
#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
n = int(input())
ord_dict = collections.OrderedDict()

for _ in range(n):
    counter= int(1)
    string = input()
    if string in ord_dict.keys():
        temp = int(ord_dict[string] + 1)
        ord_dict[string] = temp
    else:
        ord_dict[string] = counter
        
print(len(ord_dict))
res = ""
for key in ord_dict:
    res = res + str(ord_dict[key]) + " "
print(res)