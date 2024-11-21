def setop():

    #sets are like dict with its values being thrown away, leaving only key
    #sets are unordered

    #create with a set
    empty_set = set()
    even_numbers = {0, 2, 4, 6, 8}
    print(type(even_numbers))



    # #convert from other data types using set()
    new_set = set("letters")
    print(new_set)
    #
    #set from a list
    l_set = set(["Virat", "Rohit", "Shubham"])
    #
    #
    # #set from  a tuple
    # tset = set(("Virat", "Rohit", "Shubham"))
    #
    # set from  a dict
    # tset = set({"Virat": 80, "Rohit": 32, "Shubham": 90})
    # print(tset)
    # #
    # # # test for a value using in - values are set
    # #
    # players_scores = {
    #     "Rohit": {53, 87, 96},
    #     "Virat": {123, 21, 78},
    #     "Shubham": {23, 44, 85},
    # }
    #
    # for name, scores in players_scores.items():
    #         if 123 in scores:
    #             print(name)

    #
    a = {1, 2, 3}
    b = {1, 2, 3, 4}
    # print(a & b)
    # print(a.intersection(b))
    print(a | b)
    print(a.union(b))
    # print(a - b)
    # print(a.difference(b))
    # print(b - a)
    # print(b.difference(a))
    # print(a ^ b)
    # print(a.symmetric_difference(b))
    # print(a <= b) # is a subset of b
    # print(a.issubset(b))
    # print(a < b) # proper subset
    # print(a >= b)
    # print(a.issuperset(b))
    # print(a > b)
    #
    # #bigger data structures
    batsmen = ['Virat', 'Dhoni','Sachin']
    bowlers = ['Bumrah', 'Shami', 'Ashwin']
    keepers = ['Dhoni', 'Ishan']

    tuple_of_lists = batsmen, bowlers, keepers

    print(tuple_of_lists)
    #
    #
    # #tuple as a key
    houses = {(44.79, -93.14, 285): 'My house'}
    print(houses[(44.79, -93.14, 285)])




def main():
  setop()

if __name__ == "__main__":
        main()