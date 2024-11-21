def comprehension():
    #compact way of representing an iterable data structure

    number_list = []
    # number_list.append(1)
    # and so on....

    #for using range is the second method

    #pythonic way
    # list_comprehension
    # [ expression for item in iterable ]
    number_list = [ number for number in range(1,6)]
    print(number_list)

    number_list = [number - 1 for number in range(1,6)]
    print(number_list)

    #[expression for item in iterable if condition]
    number_list = [ number for number in range(1,6) if number % 2 == 1]
    print(number_list)

    #list comprehension for even numbers

    even_numbers = [ number for number in range(1,101) if number % 2 == 0]
    print(len(even_numbers))
    print(even_numbers)
    #nested loops
    # rows = range(1, 4)
    # columns = range(1, 3)
    # for rows in rows:
    #     for columns in columns:
    #         print(rows, columns)
    #
    # rows = range(1, 4)
    # cols = range(1, 3)
    # cells = [(rows, cols) for rows in rows for col in cols]
    # for cells in cells:
    #     print(cells)
    # for rows, col in cells:
    #     print(rows, col)

    # dictionary comprehension
    # {key_expression: value_expression for expression in iterable}
    # word = 'letters'
    # letter_counts = {letter: word.count(letter) for letter in word} #7 times looping
    # print(letter_counts)
    #
    # #using set to avoid duplicates
    # letter_counts = {letter: word.count(letter) for letter in set(word)} #only 5 times
    # print(letter_counts)



    #set comprehension
    # {expression for expression in iterable}

    # a_set = {number for number in range(1,6) if number % 3 == 1}
    # print(a_set)


    #no tuple comprehension but generator comprehension exists!
    #
    # number_thing =

    #comprehension example of list
    fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
    capitalized_fruits= [i.capitalize() for i in fruits  ] #capitalize will capitalize only the first letter
                                                           #title will also work
                                                           #upper will capitalize all the alphabet
    vowels = 'a','e','i','o','u'
    fruits_with_only_two_vowels = [fruits for i in fruits if fruits.count() ==2 ]


    print(capitalized_fruits)




def main():
    comprehension()

if __name__ == "__main__":
    main()