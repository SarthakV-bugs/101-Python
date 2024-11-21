# a. Using python’s open, create a file called example.txt in write mode and
# write two lines : “Hello, this is written from Python\n”, “This is the second
# line”
# b. Read the example.txt and print it line by line.
# c. Modify file contents Using readLines() and writeLines() modify the
# second line and copy back to the same file

import csv

#a.
with open('example.txt', 'w') as f:
    f.write("Hello, this is written from Python\n")
    f.write("This is the second line")

#b. using read-lines
with open("example.txt","rt") as f:
    lines=f.readlines()
    for line in lines:
           print(line.strip())

#c.
lines[1]='modifying the second line'
with open('example.txt', 'w') as f:
       f.writelines(lines)

with open('example.txt', 'r') as f:
       modified_lines = f.readlines()
       print(modified_lines)
       # for line in lines:
       #        print(line.strip())