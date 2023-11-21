""" 
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up. 

"""

#Python 3:

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    if len(arr) < 2:
        print(arr)
    else:
        mx = max(arr[0], arr[1])
        second_max = min(arr[0], arr[1])
        for i in range(2, len(arr)):
            if arr[i] > mx:
                second_max = mx
                mx = arr[i]
            elif arr[i] > second_max and mx != arr[i]:
                second_max = arr[i]
            elif mx == second_max and second_max != arr[i]:
                second_max = arr[i]
        print(second_max)
