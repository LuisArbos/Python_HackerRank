"""
Validating Credit Card Numbers

You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

Examples:

Valid Credit Card Numbers

4253625879615786
4424424424442444
5122-2368-7954-3214

Invalid Credit Card Numbers

42536258796157867       #17 digits in card number → Invalid 
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid

Input Format

The first line of input contains an integer N.
The next N lines contain credit card numbers. 
"""

#Python 3:
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    card_number = input()
    is_valid = True
    if "-" in card_number:
        if "--" in card_number:
            is_valid = False
        card_number = card_number.split("-")
        for elem in card_number:
            if len(elem) > 4:
                is_valid = False
        card_number = "".join(card_number)
    if card_number[0] != "4" and card_number[0] != "5" and card_number[0] != "6":
        is_valid = False
    if len(card_number) != 16:
        is_valid = False
    for ch in card_number:
        if not ch.isdigit():
            is_valid = False
    if re.search(r"(?<=(\d))\1{3}", re.sub(r"[^\d]", "", card_number)):
        is_valid = False
            
    if is_valid:
        print("Valid")
    else:
        print("Invalid")