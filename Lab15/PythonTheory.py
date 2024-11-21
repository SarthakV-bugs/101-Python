#












#swap two numbers
def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return (a,b)
def main():
    a = 3
    b = 4
    newA, newB = swap(a, b)
    print(newA)
    print(newB)


if __name__ == "__main__":
    #print(This is the beginning of program)
    main()
