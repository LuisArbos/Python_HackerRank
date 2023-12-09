"""
Detect HTML Tags, Attributes and Attribute Values

You are given an HTML code snippet of N lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.

Print the detected items in the following format:

Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]


The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
The > symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.

Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->). Comments can be multiline.
All attributes have an attribute value.

"""

#Python 3:
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class myHTMLParser(HTMLParser):
    def init(self):
        super().init(),
        self.inside_comment = False
    
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for i in attrs:
                print("->", i[0], ">", i[1])
    
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for i in attrs:
                print("->", i[0], ">", i[1])

parser = myHTMLParser()
for _ in range(int(input())):
    parser.feed(input())