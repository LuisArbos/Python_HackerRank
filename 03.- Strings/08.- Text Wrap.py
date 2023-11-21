""" 
Text Wrap

You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

    - string string: a long string
    - int max_width: the width to wrap to

Returns

    - string: a single string with newline characters ('\n') where the breaks should be


"""

#Python 3:

def wrap(string, max_width):
    out = [(string[i:i+max_width]) for i in range(0, len(string), max_width)]
    for i in range(len(out)-1):
        print(out[i])
    return out[len(out)-1]
