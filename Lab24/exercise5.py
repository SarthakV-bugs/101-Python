# Ex_5A
def ageCheck(age):
    age = int(input('Enter your age: '))
    if age < 0:
        raise ValueError('Negative age? No way!')
    ageIn10 = age + 10
    print('After 10 years you will be:', ageIn10)

try:
    ageCheck(-5)
except ValueError as e:
    print(e)


# Ex_5B
def divideThing(n):
    n = int(input('Type a number: '))
    try:
        if n < 0:
            raise ValueError('Negative numbers are bad!')
        result = 100 / n
        print('100 divided by', n, 'is', result)
    except ZeroDivisionError as e:
        print('You can\'t divide by zero, silly!', e)
    except ValueError as e:
        print('Oops, that\'s not a good number:', e)
    except Exception as e:
        print('Uh oh, something broke!')

divideThing(0)
divideThing(-1)
