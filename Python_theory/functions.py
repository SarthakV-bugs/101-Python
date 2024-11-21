def function():

    # def do_nothing():
    #     pass
    #
    # value=do_nothing()
    # print(value)
    # if value:
    #     print("Something")
    # else:
    #     print("Nothing")



    #positional arguments
    #values are copied to corresponding parameters
    #IMP: You need to remember the meaning of each position
    #
    # def players(bat, bowl, keep, all='Hardik'):
    #     #takes 4 parameters
    #     #all='Hardik' is a default parameter value
    #     #why do we need default parameter?
    #
    #     return {'batsmen':bat, 'bowler': bowl, 'keeper':keep, 'all rounder':all}
    #
    # #invoking positional arguments
    # p = players("rohit", 'Bumrah', 'Ishan')
    # print(p)


    #invoking keyword arguments
    #name of the parameter and the input used together to avoid error that might occur wrt position of positional parameters
    # p = players(bat='Rohit', bowl='Bumrah', keep='ishan')
    # print(p)

    #to add extra parameters in an already defined function with set parameters
    #write a function such that it can take 'variable number of parameters'

    ####(*args)
    #when used inside the function with a parameter,
    #an asterisk groups a variable no. of parameters.


    # def print_args(*args):
    #
    #     print('positional argument tuple:', args)
    #
    # print_args()
    # print_args(3, 2, 1, 'wait!', 'uh..')
    # print_args('Rohit', 'Rahul' , 'Virat', 'Gill', 'Jadeja')

    #if your function has required positional arguments as well, and variable number of args with *args
    #
    # def print_more(required1, required2, *args):
    #     print('Need this one:', required1, type(required1))
    #     print('Need this too:', required2, type(required2))
    #     print('All the rest',args, type(args))
    #
    #
    #
    # #**kwargs
    # def print_kwargs(**kwargs):
    #  print('keyword arguments:', kwargs, type(kwargs))
    #  print(kwargs.keys())
    #
    #
    # #gather keyword arguments with **
    #
    #
    #
    # def add_args(arg1, arg2):
    #     print(arg1+arg2)
    # def run_something_with_args(func, arg1, arg2):
    #     func(arg1,arg2)
    #
    # #passing functions as a parameter within a function
    #
    # type(add_args)
    # run_something_with_args(add_args,4,5)
    #
    # def outer(a,b):
    #     def inner(c,d):
    #         return c+d
    #     return inner(a,b)
    #
    #
    #
    # #inner functions
    # print(outer(2,3))
    #
    # #
    # def knights2(saying):
    #     def inner2():
    #         return 'We are the knights who say: %s' % saying
    #     return inner2()
    #
    # #closures
    # a = knights2('Duck')
    # b = knights2('chicken')
    # print(type(a))
    # print(a())

###LAMBDA FUNCTION
def square_numbers(numbers,func):
    for number in numbers:
        print(func(numbers))

def square_func(x):
    return x*x

numbers = [1,2,3,4,5]
square_numbers(numbers,square_func)




#lambda takes one argument, which we call word here.
#everything between the colon and the terminating parentheses is the
square_numbers(numbers, lambda n: n ** 2)









def main():
    function()

if __name__ == "__main__":
    main()