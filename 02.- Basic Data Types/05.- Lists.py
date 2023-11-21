""" 
Lists

Consider a list (list = []). You can perform the following commands:
	1.- insert i e: Insert integer e at position i.
	2.- print: Print the list.
	3.- remove e: Delete the first occurrence of integer e.
	4.- append e: Insert integer e at the end of the list.
    	5.- sort: Sort the list.
    	6.- pop: Pop the last element from the list.
    	7.- reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list. 

"""

#Python 3:

if __name__ == '__main__':
    N = int(input())
    li = []
    for i in range(N):
        command = input()
        command_0 = command.split(' ')[0]
        if command_0 == "insert" or command_0 == "remove" or command_0 == "append":
            command_1 = int(command.split(' ')[1])
            if command_0 == "insert":
                command_2 = int(command.split(' ')[2])
        match command_0:
            case "insert":
                li.insert(command_1, command_2)
            case "print":
                print(li)
            case "remove":
                li.remove(command_1)
            case "append":
                li.append(command_1)
            case "sort":
                li.sort()
            case "pop":
                li.pop()
            case "reverse":
                li.reverse()
            case _:
                print("Wrong command")
