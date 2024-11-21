def calculator(N1,N2,O):
    try:
        if O=="+":
            print(f"Addition of {N1} and {N2}: {float(N1)+float(N2)}")
        elif O=="-":
            print(f"Subtraction of {N1} and {N2}: {float(N1)-float(N2)}")
        elif O == "/":
            print(f"Division of {N1} and {N2}: {float(N1)/float(N2)}")
        elif O == "*":
            print(f"Multiplication of {N1} and {N2}: {float(N1)*float(N2)}")
        else:
            raise ValueError("Operator not defined! Use (+, -, /, *)")
    except (ZeroDivisionError, ValueError) as err:
        print("Cannot perform operation! Error type:",err)
def main():
    n1=input("Enter number1: ")
    n2=input("Enter number2: ")
    op=input("Enter the operator (+, -, /, *): ")
    if op not in ['+','-','*','/']:
        print('operator not defined')
    else:
        calculator(n1, n2, op)


if __name__=="__main__":
    main()