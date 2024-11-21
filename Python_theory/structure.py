

def basics():

    #line continuation using \ character
    # alphabet = 'abcdefg' + \
#     #        ''
#
#     vowels = 'aeiou'
#     letter = 'o'
#     if letter in vowels:
#         print(letter, 'is a vowel')
#
#     #in works with all iterables (list,tuples,etc)
#
#     vowel_dict = {'a': 'apple', 'e': 'elephant', 'i': 'impala'}
#     print(letter in vowel_dict)
#
#
#
#     #while loop
#     # while True creates an infinite loop, infinite loop with break, look into continue
#     #while and else loop
#     numbers = [1,2,3]
#     position = 0
#     #
#     # while
#     #
#     # else
#
#
#
#
#
#
# ###iterations
#     players = ["Rohit", "Gill", "Virat", "Rahul"]
#     current = 0
#     while current < len(players):
#         print(players[current])
#         current+= 1
#     #pythonic way
#     for x in players:
#         print(x)

#string iteration
#strings produce a character

    # word = 'cat'
    # for letter in word:

    # players = {"bowler": bumrah}

    #return both key and value in a tuple
    # for item in players.items():
    #     print(item)
    #
    # for type, name in players.items():
    #     print(type, name)



    #
    # odd_list = [1, 3, 5, 7]
    # even_list = [2, 4, 6, 8]
    # prime_list = [2, 3, 5, 7, 11]
    # #find sum of first elements of all by checking the length, we can iterate through  the shortest length list...
    # for odd_list, even_list, prime_list in zip(odd_list, even_list, prime_list):
    #         # sum= odd_list + even_list + prime_list
    #         # print(sum)
    # # iterate triple sequences with zip
    # days = ['Monday', 'Tuesday', 'Wednesday']
    # fruits = ['Banana', 'Apple', 'orange']
    # drinks = ['coffee', 'tea', 'milk']
    # desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
    #
    # for days, fruits, drinks, desserts in zip(days, fruits, drinks, desserts):
    #     print(days, ":drink", drinks, "-eat", fruits, "-enjoy", desserts)
    #zip() stops when the shortest sequence is done
    #therefore no puddings until we extend the lists




    #machine translate function

    en_list= ["Monday", "tuesday", "Wednesday"]
    fr_list= ["Lundi", "Mardi", "Mercredi"]
    #return a dict that maps english word to French word

    eng_to_fre = {}
    for en_list, fr_list in zip(en_list, fr_list):

    #range function
    #like zip() range returns an iterable object

    for x in range(0, 3):
        print(x)

    print(list(range(0, 3)))

    #range is exclusive of the stop
    for x in range(2, -1 , -1):
        print(x)

    print(list(range(2, -1 , -1)))



def main():
   basics()

if __name__ == "__main__":
    main()