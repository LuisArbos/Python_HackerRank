""" 
Designer Door Mat

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

    - Mat size must be NxM (N is an odd natural number, and M is 3 times N.)
    - The design should have 'WELCOME' written in the center.
    - The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------


"""

#Python 3:

if __name__ == '__main__':
    data = input()
    data = data.split(" ")
    n = int(data[0])
    m = int(data[1])
    for i in range((n//2)):
        string = ".|."
        if i == 0:
            print(str(string*1).center(m, "-"))
        else:
            print(str(string*(2*i+1)).center(m, "-"))
    welcome = "WELCOME"
    print(welcome.center(m, "-"))
    for i in range((n//2)):
        string = ".|."
        if i == 0:
            print(str(string*(n-2)).center(m, "-"))
        else:
            print(str(string*(n-(2*(i+1)))).center(m, "-"))

