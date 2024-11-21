
dic1={"Jane Austen":["Pride and Prejudice","Sense and Sensibility"],
      "Charles Dickens":["Oliver Twist","Pickwick Papers"]}
import time
def addpreface(func):
    def wrapper(*arg):
        print("the author is:",arg)
        print("these authors are of classical literature ")
        func(*arg)
        print("they are to be enjoyed")
    return wrapper
@addpreface
def Listbookbyauthor(authors):
    for author in authors:
        print(author)
        print(dic1[author])


def logexcuete(func):
    def wrapper(*arg):
        print(f"entering function add two numbers at time {time.time()}")
        func(*arg)
        print(f"exting function add two numbers at time{time.time()}")
    return wrapper
@logexcuete
def addnumbers(a,b):
   print(a+b)



def main():
    auth=input("Enter the name of author: ")
    print(auth.split(','))
    Listbookbyauthor(auth.split(','))
    number1=int(input("Enter the first number: "))
    number2=int(input("Enter the second number: "))
    print(addnumbers(number1,number2))

if __name__ == '__main__':
    main()