"""
Piling Up!

There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube[i] is on top of cube[j] then sideLength[j] >= sideLength[i].

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example

blocks = [1,2,3,8,7]

Result: No

After choosing the rightmost element, 7, choose the leftmost element, 1. After than, the choices are 2 and 8. These are both larger than the top block of size 1.

blocks = [1,2,3,7,8]

Result: Yes

Choose blocks from right to left in order to successfully stack the blocks.

Input Format

The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order. 

Output Format

For each test case, output a single line containing either Yes or No.

"""
#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    block_size, blocks = int(input()), list(map(int, input().split()))
    result = True
    prev = float("inf")
    while block_size > 0:
        left, right = blocks[0], blocks[block_size-1]
        
        if left == right and prev >= left:
            blocks.pop()
            prev = left
        elif left > right and left <= prev:
            blocks.pop()
            prev = left
        elif right > left and right <= prev:
            blocks.pop(block_size-1)
            prev = right
        else:
            result = False
            break
        block_size -= 1
    if result:
        print("Yes")
    else:
        print("No")
