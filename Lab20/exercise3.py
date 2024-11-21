# Write a function course_info(name, stream="BDB", batch="2024", **kwargs). This should
# print the values of all the arguments passed including the mandatory and default
# arguments. The variable argument dictionary kwargs should be iterated and both the key
# and values printed.
#
# Call the function using :
# a. Only mandatory argument (name)
# b. Mandatory argument (name) and overriding default argument
# (stream=”BTBI”, batch=”2023”)
# c. Mandatory argument, kwargs as follows : facilitator, type
# d. Mandatory argument, overriding default argument
# stream=”2020”, kwargs as follows : facilitator, location

def course_info(name, stream="BDB", batch="2024", **kwargs):
    print(f'name: {name}')
    print(f'stream: {stream}')
    print(f'batch: {batch}')
    for key,value in kwargs.items():

        print(f'{key}:{value}')


def main():
    names_input = input("Enter the name of student: ")
    facilitator = input("Enter the name of facilitator: ")
    subject = input("Enter the name of subject: ")

    names = [name for name in names_input.split(',')]
    for name in names:
        course_info(name)
        course_info(name,stream='BTBI',batch='2023')
        course_info(name, facilitator=facilitator, type=subject)
        course_info(name, stream='2020', facilitator=facilitator, location='third floor')



if __name__ == "__main__":
        main()