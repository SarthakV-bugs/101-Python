def is_prime(num):

    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def nextPrime(n):

    next_number = n + 1
    while not is_prime(next_number):
        next_number += 1
    return next_number


def main():

    n = int(input("Enter an integer: "))

    prime = nextPrime(n)
    print(f"The first prime number larger than {n} is {prime}.")


if __name__ == "__main__":
    main()
