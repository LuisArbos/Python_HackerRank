""" 
The Minion Game

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

    - string string: the string to analyze

Prints

    - string: the winner's name and score, separated by a space on one line, or Draw if there is no winner


"""

#Python 3:

def minion_game(string):
    # your code goes here
    length = len(string)
    k_score = 0
    s_score = 0
    for i in range(length):
        if string[i] in ["A", "E", "I", "O", "U"]:
            k_score += (length - i)
        else:
            s_score += (length - i)
    if k_score > s_score:
        print("Kevin", k_score)
    elif k_score == s_score:
        print("Draw")
    else:
        print("Stuart", s_score)
    