"""
XML 2 - Find the Maximum Depth

You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as 0.

Input Format

The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.

"""
#Python 3:
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    elements = list(elem.iter())

    if len(elements) == 1:
        maxdepth = max(maxdepth, level+1)
    else:
        for i in range(1, len(elements)):
            depth(elements[i], level+1)
    
    return maxdepth

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


    