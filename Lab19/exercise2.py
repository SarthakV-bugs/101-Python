#Create a list with a random length between 100 and 200 - Say 149 elements.
# Create random numbers for this list. Print the first half and second half of this
# list using slicing.
# In the list created above , print the elements occurring more than once and
# those elements that are unique. Use set

import random

random_list = [random.randint(100, 200) for i in range(1,150)]  #for _ in range(1,150)
print(random_list)
l = len(random_list)
print(l)

first_half = random_list[: l//2]
second_half = random_list[l//2 :]

print(first_half)
print(second_half)

#duplicate elements
dupl_elements = set([num for num in random_list if random_list.count(num) > 1])
print(dupl_elements)

#unique elements

uniq_elements = set(random_list) - dupl_elements         #set a - set b #dupl_elements is already a set
print(uniq_elements)


