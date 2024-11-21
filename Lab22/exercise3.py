# Define a function apply_operation(a,b,operation) where operation is a lambda function.
# Inside apply_operation, call the operation(a,b) and return the output. Define the lambda
# functions sum, quotient, product (from Ex 1a) and difference for the two lists list_1, list_2
# similar to ex. 1 and print the output.
from functools import reduce

from Lab22.exercise1 import list_1, list_2


def calculator(a,b,operation):
    return operation(a,b)

product = lambda x,y:x*y
summation = lambda  x,y:x+y
difference = lambda x,y:x-y
quotient =  lambda x,y:x//y
remainder = lambda x,y:x%y



print([calculator(a,b,product)for a,b in zip(list_1,list_2)])
print([calculator(a,b,summation)for a,b in zip(list_1,list_2)])
print([calculator(a,b,difference)for a,b in zip(list_1,list_2)])
print([calculator(a,b,quotient)for a,b in zip(list_1,list_2)])
print([calculator(a,b,remainder)for a,b in zip(list_1,list_2)])
