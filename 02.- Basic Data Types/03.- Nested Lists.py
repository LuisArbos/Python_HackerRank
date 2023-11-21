""" 
Nested Lists

Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

"""

#Python 3:

if __name__ == '__main__':
    full_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        full_list.append((name, score))
        full_list.sort(key=lambda k: (k[1], k[0]))
    lowest = full_list[0][1]
    second_lowest = full_list[1][1]
    pos_second_lowest = 1

    for i in range(1, len(full_list)):
        if second_lowest == lowest:
            second_lowest = full_list[i][1]
            pos_second_lowest = i
    for i in range(0, len(full_list)):
        if full_list[i][1] == second_lowest:
            print(full_list[i][0])
    
    
