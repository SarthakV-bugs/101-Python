#global scope and local scope of namespace
#global scope. the variable is accessible to all parts of the prog
#local scope: local to the program it is defined in
#amazing.__name__



gname = 'INDIA'


def compute_tax():
    # global gname
    lname = 'karnataka'
    print(lname)
    # print(gname) #if we put print before updating the variable locally, we'll get an error
    gname = 'my_India'  # created a local variable
    print(gname)


def compute_salary():
    print(gname)
    # print(lname)

def try_except():
    short_list = [1,2,3]
    position = 5
    try:
        print(short_list[position])
    except:
        print()

#difference between if/else and try/except
#using try/except is an expensive process for the compiler
#know when to use it
# another example

    while True:
        value = input('position[q to quit]? ')
        if value == 'q':
            break
        try:
            position = int(value)
            print(short_list[position])
        except IndexError as err:
            print('Bad index:' , position)
        except Exception as other:
            print('something else broke:', other)


def main():
    compute_tax()
    compute_salary()
    try_except()




if __name__ == "__main__":
        main()