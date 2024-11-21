# a. Using python’s csv library, create a csv file (students.csv) with the
# following values:
#
# Name,Age,City
# Alice,25,New York
# Bob,30,Los Angeles
# Charlie,35,Chicago
#
# b. Read the states_by_country.csv and print the set of all unique countries.

import csv
from enum import unique

details=[["Name","Age","City"],
["Alice",25,"New York"],
["Bob",30,"Los Angeles"],
["Charlie",35,"Chicago"]]

#a.
with open('students.csv', 'wt') as file:
    csvfile = csv.writer(file)
    csvfile.writerows(details)

with open('students.csv', 'rt') as file:
    csvfile = csv.reader(file)
    for line in csvfile:
        print(line)


#b.

unique_countries=[]
with open('states_by_country.csv','rt') as f:   #store the file in the current folder
    csvfile=csv.reader(f)
    for line in csvfile:
        unique_countries.append(line[3])
print(set(unique_countries))


