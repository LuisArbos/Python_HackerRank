"""
Decorators 2 - Name Directory

Let's use decorators to build a name directory! You are given some information about N people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

For Henry Davids, the output should be:

Mr. Henry Davids

For Mary George, the output should be:

Ms. Mary George

Input Format

The first line contains the integer N, the number of people.
N lines follow each containing the space separated values of the first name, last name, age and sex, respectively. 
"""

#Python 3:
import operator

def person_lister(f):
    def inner(people):
        result = []
        for i in range(len(people)):
            people[i][2] = int(people[i][2])
        people.sort(key=operator.itemgetter(2))
        for i in people:
            result.append(f(i))
        return result
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
