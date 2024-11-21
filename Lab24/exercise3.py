counter1 = 1
shared_value = 5


def log_decorator(func):
    def wrapper(n):
        global shared_value
        func(n)
        print("After calling", func.__name__, "with", n, "shared_value =", shared_value)

    return wrapper


@log_decorator
def add_to_shared_value(n):
    global shared_value
    shared_value += n


@log_decorator
def multiply_shared_value(n):
    global shared_value
    shared_value *= n


def incrementglob(func):
    def wrapper():
        global counter1
        counter1 = counter1 + 1
        return func()

    return wrapper


@incrementglob
def glob_counter():
    return counter1


def local_counter(num):
    global counter1
    counter1 = num
    return counter1


def main():
    n = int(input("Enter a number for the Local counter: "))
    for i in range(5):
        print("Local counter =", local_counter(n))
        print("Global counter =", glob_counter())

    n1 = int(input("Enter a number for the shared value operations: "))
    for i in range(n1):
        add_to_shared_value(i)
        multiply_shared_value(i)


if __name__ == "__main__":
    main()
