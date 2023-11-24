""" 
Find Angle MBC

ABC is a right triangle, 90º at B. Therefore, ABC = 90º.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find MBC in degrees.

Input Format

The first line contains the length of side AB.
The second line contains the length of side BC. 

Output Format

Output MBC in degrees.

Note: Round the angle to the nearest integer.

"""

#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = int(input())
BC = int(input())
result = str(round(math.degrees(math.atan(AB/BC)))) + u"\u00b0"
print(result)

