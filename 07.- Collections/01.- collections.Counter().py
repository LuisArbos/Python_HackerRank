"""
collections.Counter()

A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

Example:

>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

Task

Raghu is a shoe shop owner. His shop has X number of shoes. He has a list containing the size of each shoe he has in his shop. There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Input Format

The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.


"""
#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
X, shoe, N = int(input()), list(map(int, input().split())), int(input())
shoe_counter = collections.Counter(shoe)
result = 0
for i in range(N):
    size, price = map(int, input().split())
    if size in shoe_counter.keys() and shoe_counter[size] > 0:
        result += price
        shoe_counter[size] -= 1
print(result)
