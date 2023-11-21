""" 
Alphabet Rangoli

You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------

The center of the rangoli has the first alphabet letter a, and the boundary has the N^th alphabet letter (in alphabetical order).

Function Description

Complete the rangoli function in the editor below.

rangoli has the following parameters:

    - int size: the size of the rangoli

Returns

    - string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)

"""

#Python 3:

def print_rangoli(size):
    # your code goes here
    new_size = (size * 2 - 1) * 2 - 1
    string = "abcdefghijklmnopqrstuvwxyz"
    new_string = string[:size][::-1]
    final_string = []
    for i in range(1, len(new_string)+1):
        half = "-".join(new_string[0:i])
        half += half[:-1][::-1]
        final_string.append(half.center(new_size, "-"))
    final_string.extend(final_string[:-1][::-1])
    for i in final_string:
        print(i)
