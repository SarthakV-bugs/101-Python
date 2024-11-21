# A. Write a generator function fibonacci that yields the Fibonacci series number infinitely.
# Create a generator expression fib_gen that calls this function. Print the 10 numbers of
# this generator expression using next()
# B. Repeat the same for generating even_numbers

def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a1 =a
        a = b
        b = a1 + b

def even_numbers():
    i=1
    while True:
        if i % 2 == 0:
            yield i
        i+=1


def main():
    n = int(input("enter the number for fibonacci and even number: "))
    fib_gen = fibonacci()
    for i in range(n):
     print(next(fib_gen))

    even_nu = even_numbers()
    for i in range(n):
        print(next(even_nu), end=' ')
    print()

if __name__ == "__main__":
    main()


