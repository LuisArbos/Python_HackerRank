""" 
Capitalize!

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck. Given a full name, your task is to capitalize the name appropriately.

"""

#Python 3:

def solve(s):
    new_s = ""
    new_s += s[:1].upper()

    for i in range(1, len(s)):
        if s[i-1].isspace() and not s[i].isspace():
            new_s += s[i:i+1].upper()
        elif s[i-1].isspace() and s[i].isspace():
            new_s += " "
        else:
            new_s += s[i:i+1]
            
    return new_s
