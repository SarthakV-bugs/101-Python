# 4. Create a function create_exponent that takes n as a parameter and returns a lambda
# function that is x raised to the power n.
# Create two functions create_4th_exponent and create_5th exponent that calls
# create_exponent with powers 4, 5 .
# For every element in list_1 (created as in ex. 1a) call create_4th_exponent,
# create_5th_exponent and print the output list.
from Lab22.exercise1 import list_1


def create_exponent(n):
    return lambda x: x**n

create_4th_exponent =create_exponent(4)
create_5th_exponent = create_exponent(5)

print([create_4th_exponent(x)for x in list_1])
print([create_5th_exponent(x)for x in list_1])

