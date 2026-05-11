"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

file = open("./resources/names.txt","r")
content = file.read().strip('"').split('","')
content.sort()
# offset by 64
res = 0
for i in range(len(content)):
    name = content[i]
    name_val = 0
    # get value of name
    for c in name:
        name_val += ord(c) - 64
    res += (name_val) * (i + 1)

print(res)