"""
Validating UID

ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

    - It must contain at least 2 uppercase English alphabet characters.
    - It must contain at least 3 digits (0-9).
    - It should only contain alphanumeric characters (a-z, A-Z & 0-9).
    - No character should repeat.
    - There must be exactly 10 characters in a valid UID.

Input Format

The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.
"""

#Python 3:
# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    is_valid = True
    unique_uid = input()
    new_set = set(unique_uid)
    digit_counter, cletter_counter = 0, 0
    if len(unique_uid) != 10 or len(new_set) != 10:
        is_valid = False
    else:
        for ch in unique_uid:
            if ch.isnumeric():
                digit_counter += 1
            elif ch.isalpha() and ch.isupper():
                cletter_counter += 1
            elif not ch.isalnum():
                is_valid = False
                break
        if digit_counter < 3 or cletter_counter < 2:
            is_valid = False
    if is_valid:
        print("Valid")
    else:
        print("Invalid")