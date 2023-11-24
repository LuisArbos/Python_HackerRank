""" 
Set.add()

If we want to add a single element to an existing set, we can use the .add() operation.
It adds the element to the set and returns 'None'.

Task

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.

Input Format

The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from. 

"""

#Python 3:

N = int(input())
total_set = set()
for i in range(N):
    total_set.add(input())
print(len(total_set))

