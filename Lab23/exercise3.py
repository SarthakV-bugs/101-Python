# 3. A. Create two functions AddNumbers(x,y) and SubtractNumbers(x,y) that add/subtract
# the two numbers respectively. Create a function OperateNumbers that takes
# AddNumbers / SubtractNumbers as argument and invokes the function passed as
# argument with default values.
# B. Repeat the above for the operations on strings (ConcatenateStrings(str1, str2) and
# ReplaceWord(str1, str2=”” and OperateStrings(func) )
from PIL.ImageChops import subtract


def AddNumbers(x,y):
    return x+y

def SubtractNumbers(x, y):
    return x-y

# def operate(func):
#     return func()

def OperateNumbers(func,x,y):
    result = func(x,y)
    print(result)

def concatenate_strings(str1,str2):
    str1+=str2
    return str1

def replace_word(str1,str2):
    str1= str1.replace('something',str2)
    return str1

def operate_str(func,str1,str2):
    result = func(str1,str2)
    print(result)

def main():
    # print(operate(SubtractNumbers(2,3)))
    OperateNumbers(SubtractNumbers,2,3)
    OperateNumbers(AddNumbers,10,20)

    operate_str(concatenate_strings,'hello', 'world')
    operate_str(replace_word,'hello something', 'Sarthak world')


if __name__ == "__main__":
    main()