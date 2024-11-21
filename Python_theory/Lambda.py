def functions():

    def iterate_numbers(numbers,func):
        for number in numbers:
         print(func(number))

    def square_func(n):
        return n ** 2

    numbers = [1,2,3,4,5]
    iterate_numbers(numbers,square_func)




    #lambda takes one argument, which we call word here.
    #everything between the colon and the terminating parentheses is the
    iterate_numbers(numbers, lambda n: n ** 2)   #instead of passing square function, we pass lambda

    #problem

    location = 'Bangalore'
    upper = lambda string_val: location.upper()
    print(type(upper))          #type = func
    print(upper(location))

    #problem

    cube_of_number = (lambda n: n **  3)
    print(cube_of_number(5))

    # is_even_list

    is_even_list = [lambda arg=x: arg*10 for x in range(0,5)]
    # is_even_list = [lambda arg=x: x * 10 for x in range(0, 5)]
    print(is_even_list) #will give five functions


    for item in is_even_list:
        print(item())



    #passing the function as a parameter





def main():
    functions()

if __name__ == "__main__":
    main()