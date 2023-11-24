""" 
No Idea!

There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i in A, you add 1 to your happiness. If i in B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Input Format

The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7

Sample Output

1

Explanation

You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B. The element 7 in set B does not exist in the array so it is not included in the calculation.

Hence, the total happiness is 2-1 = 1.

"""

#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
first_line = list(input().split(" "))
arr = list(input().split(" "))
A_list = list(input().split(" "))
B_list = list(input().split(" "))
A_set = set()
B_set = set()
result = 0

for i in range(len(A_list)):
    A_set.add(A_list[i])
for i in range(len(B_list)):
    B_set.add(B_list[i])

for i in range(len(arr)):
    if arr[i] in A_set:
        result += 1
    if arr[i] in B_set:
        result -= 1

print(result)