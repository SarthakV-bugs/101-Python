# 1. Create two lists list_1, list_2 with 100 random numbers between 0 and 100. Create the
# following lambda functions and print them :
# a. Product -(of each element of list_1 and list_2, use zip)
# b. Square - (of each element of list_1)
# c. Cube - (of each element of list_1)
# d. Even - A list of booleans (True of list_1 is even)
# e. Even_list : use filter and the even lambda function to filter out only the even
# elements from list_1
# f. Square_cube: use the lambda functions b and c to compose a new function
# passing the cube of each element in list_1 to the square function.

import random

list_1 = [random.randint(0, 100) for i in range(1,100)]
print(list_1)

list_2 = [random.randint(0, 100) for i in range(1,100)]
print(list_2)

product = lambda x,y:x*y
print([product(x,y)for x,y in zip(list_1,list_2)])

square = lambda x: x**2
print([square(i) for i in list_1])

cube = lambda x: x**3
print([cube(i) for i in list_1])

even = lambda x:True if x%2 ==0 else False
print([even(i) for i in list_1])

odd = lambda x:True if x%2 ==1 else False
print([odd(i) for i in list_1])

filter_even = list(filter(even,list_1))
print(filter_even)

square_cube = lambda x: square(cube(x))
print([square_cube(i) for i in list_1])







