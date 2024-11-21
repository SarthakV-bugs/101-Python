def get_ordinal_number(n):
        if n == 1:
            return "first"
        elif n == 2:
            return "second"
        elif n == 3:
            return "third"
        elif n == 4:
            return "fourth"
        elif n == 5:
            return "fifth"
        elif n == 6:
            return "sixth"
        elif n == 7:
            return "seventh"
        elif n == 8:
            return "eighth"
        elif n == 9:
            return "ninth"
        elif n == 10:
            return "tenth"
        elif n == 11:
            return "eleventh"
        else:
            return "twelfth"



def main():
    for i in range(1,13):
        print(f"{i}: {get_ordinal_number(i)}")


if __name__ == "__main__":
    main()













