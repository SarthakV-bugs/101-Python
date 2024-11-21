# Use list comprehension to print the squares of even numbers and cubes of
# odd numbers for a list of randomly generated 100 numbers.
import random

# Generate a list of 100 unique random numbers between 1 and 100
# random_num = []
#
# for i in range(100):
#     number = random.randint(1,100)
#     random_num.append(number)
#
# print(random_num)

#
random_list = [random.randint(1,100) for i in range(1,100)]
print(random_list)

sq = [num**2 for num in random_list if num%2==0 ]

cube = [num**3 for num in random_list if num%2 != 0]

sq_cube = [(num ** 2 if num % 2==0 else num**3)for num in random_list]

print(sq)
print(cube)
print(sq_cube)