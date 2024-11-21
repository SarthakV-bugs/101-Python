def IsInteger(s):
    # Strip any leading and trailing whitespace from the input string
    s=s.strip()
    #Check if the string has more than one character and starts with '+' or '-',
    if len(s) > 1 and (s[0]=='+' or s[0]=='-') and s[1:].isdigit():
        return True
    # If the string does not start with '+' or '-', check if the entire string consists of digits
    elif s.isdigit():
        return True
    else:
        return False
def main():
    str=input("Enter the string: ")
    if IsInteger(str):
        print("The string",str,"is an integer")
    else:
        print("The string",str,"is not an integer")

if __name__== "__main__" :
    main()