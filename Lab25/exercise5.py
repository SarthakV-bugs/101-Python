class AgeTooYoungError(Exception):
  pass
def CheckAge(a):
    try:
        if a<18:
            raise AgeTooYoungError("Age must be above 18!")
        else:
            print('you are an adult')
    except AgeTooYoungError as Err:
        print("Error type: ",Err)
try:
    # Age=int(input('Enter the age that you want to check: '))
    # CheckAge(Age)
    CheckAge(3)
except ValueError as Err1:
    print("Error type: ",Err1)
