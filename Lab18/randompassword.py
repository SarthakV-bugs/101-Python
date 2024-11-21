from random import randint


def random_password_generator():

    l= randint(7,10)
    password = ''

    # for i in range(l):
    #     char = chr(randint(33,126))
    #     password=password+char
    # return password

    i=0
    while i < l:
        char = chr(randint(33,126))
        password=password+char
        i = i+1
    return password



def main():
    print("The random password is:", random_password_generator())

if __name__ == "__main__":
    main()