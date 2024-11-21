#why do we need decorators?
#decorator is also a type of function
#decorates some other function to provide additional functionalities to that function.
import time
import math


def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper






@decorator
def say_whee():
    print("Whee!")

# say_whee = decorator(say_whee)

#decorator to calculate time elapsed

def calculate_time(func):
        def inner1(*args, **kwarg):
            begin=time.time()

            func(args, **kwarg)
            #storing time after func execution
            end = time.time()
            print("Total time taken in:", func.__name__,end - begin)

        return inner1

@calculate_time
def fact(num):
    time.sleep(2)
    print(math.factorial(num))


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print('before execution')

        returned_value = func(*args, **kwargs)
        print('after execution')

        return returned_value
    return inner1


def add(a,b):




def main():

    say_whee()
    fact(4)






if __name__ == "__main__":
        main()
