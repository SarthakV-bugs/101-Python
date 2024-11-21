# Create a function that takes an integer between 0 and 999 as its only parameter, and returns a
# string containing the English words for that number. For example, if the parameter to the
# function is 142 then your function should return “one hundred and forty-two”. Use one or more
# dictionaries to implement your solution. Include a main program that reads an integer from the
# user and displays its value in English words. Use Inner functions, lambda functions and
# positional, default arguments.

def num_to_word(n):
    ones_hund_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    tens_dict = {1: {0: 'tens',
                     1: 'eleven',
                     2: 'twelve',
                     3: 'thirteen',
                     4: 'fourteen',
                     5: 'fifteen',
                     6: 'sixteen',
                     7: 'seventeen',
                     8: 'eighteen',
                     9: 'nineteen'
                     },
                 2: 'twenty',
                 3: 'thirty',
                 4: 'forty',
                 5: 'fifty',
                 6: 'sixty',
                 7: 'seventy',
                 8: 'eighty',
                 9: 'ninety'
                 }

    def tens(n):
        if n==10:
            return 'ten'
        if n < 10:
            return ones_hund_dict[n]
        if n%10==0:
            return tens_dict[n//10]         #for (20,30,etc)
        elif n//10==1:          #if quotient is 1, for '-teens'
            return tens_dict[1][n%10]
        else:
             return tens_dict[n//10]+'-'+ones_hund_dict[n%10] #for (23,etc)

    def hundreds(n):

        hundred = ones_hund_dict[n // 100] + 'hundred'
        rem_dig = n % 100 #like for 213,etc

        if rem_dig == 0:  #like 200,etc
            return hundred
        else:
            return f"{hundred} and {tens(rem_dig)}"
    if n < 0 or n > 999:
        return "not in range"  # to check for negative number or number more than 3 dig
    if n == 0:
        return "zero"  # to check for zero
    if n < 100:
        return tens(n).capitalize()
    else:
        return hundreds(n).capitalize()

def main():
    n = int(input("Enter the number: "))

    print(num_to_word(n))



if __name__ == "__main__":
        main()


