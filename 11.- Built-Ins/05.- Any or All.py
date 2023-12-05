"""
Any or All

any()

This expression returns True if any element of the iterable is true.
If the iterable is empty, it will return False.

Sample Code
>>> any([1>0,1==0,1<0])
True
>>> any([1<0,2<1,3<2])
False

all()

This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.

Sample Code
>>> all(['a'<'b','b'<'c'])
True
>>> all(['a'<'b','c'<'b'])
False

Task

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

"""
#Python 3:
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
integers = list(map(int, input().split()))
print(all([int(i)>0 for i in integers]) and any([str(j) == str(j)[::-1] for j in integers]))
       



    