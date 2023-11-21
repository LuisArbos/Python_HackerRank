""" 
Loops

The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i^2. 

"""

#Python 3:

if __name__ == '__main__':
    n = int(input())
    if n > 0:
        for i in range(n):
            print(i*i)
        