#checkforoddeven

def check_odd_even(n):
    if n % 2 == 0:
       return "even"
    else:
        return "odd"


def main():
    n=6

    out=check_odd_even(n)
    print(out)




if __name__ == "__main__":

    main()