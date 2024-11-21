def repeat(n_times):
    def repeat_greet(func):
        def wrapper(args):
            sum=func(args)*n_times
            return sum
        return wrapper
    return repeat_greet

def upper_case_greet(func):
    def wrapper(args):
        args=args.upper()
        return func(args)
    return wrapper

message=input("Please enter a message: ")
n=int(input("Enter the number of times you want to print the message: "))
@repeat(n)
@upper_case_greet
def greet(message):
    return message

def main():
    print(greet(message))

if __name__=="__main__":
    main()

