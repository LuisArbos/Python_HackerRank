"""
Collections.OrderedDict()

An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

Example

Code

>>> from collections import OrderedDict
>>> 
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>> 
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>> 
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>> 
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

Task

You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence. 


"""
#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

N = int(input())
ord_dict = collections.OrderedDict()
for _ in range(N):
    li_inp = list(input().split())
    item_name = ""
    item_price = 0
    for i in range(0, len(li_inp)):
        if i == int(len(li_inp)-1):
            item_price = int(li_inp[i])
        else:
            if i > 0:
                item_name = item_name +" "+ str(li_inp[i])
            else:
                item_name = str(li_inp[i])
    if item_name in ord_dict.keys():
        ord_dict[item_name] += item_price
    else:
        ord_dict[item_name] = item_price
for key in ord_dict:
    print(key, ord_dict[key])

