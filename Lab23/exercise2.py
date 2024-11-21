# 2. A. Create a list of numbers from 1 to 10. Create a list squares_list using comprehension
# for the squares of the numbers (squares_list) . Create a generator expression for the
# same (squares_gen) . Print squares_list and squares_gen and observe the difference.
# Iterate over both and print the values.
# B. Repeat the above for a list/generator expression of even numbers
def square_num():
    sq_list = [i*i for i in range(1,11)] #list comprehension
    sq_gen = (i*i for i in range(1,11)) #gen expression with parentheses


    print(sq_list)
    print(sq_gen) #gives the hexadecimal location of gen obj

    # to print the sq_gen, we need to iterate using for loop
    for i in sq_gen:
        print(i)

def even_num():
    even_list = [i for i in range(1,21) if i%2 == 0]
    even_gen = (i for i in range(1,21) if i%2 == 0)


    print(even_list)
    print(even_gen)
    
    even_gen_print = [i for i in even_gen]
    print(even_gen_print)
    # for i in even_gen:
    #     print(i)

def main():
    square_num()
    even_num()



if __name__ == "__main__":
    main()