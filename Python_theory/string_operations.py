def string_operations():
    s="Welcome to Python programming"
    # print(s[:])
    # print(s[0])
    # print(s[-1])
    # print(s[5:])
    # print(s[2:5])
    # print(s[0:9:2])
    # print(s[-3:])
    # print(s[::-1])
    # print(s[18:-3])
    # print(s[-6:-2])
    # print(s[::7])
    # print(s[-1::-1])
    # print(s[-150:])

    #string length
    string_length = len(s)
    print(string_length)

    #split based on delimiter
    #why s.split?
    tokens = s.split(" ")
    print(tokens)

    #join the split tokens
    s1 = ''.join(tokens)
    print(s1)

    #check if a string starts with some other string
    #for checking the end use endswith
    s2 = s.startswith("Welcome")
    print(s2)

    s2 = s.startswith("python")
    print(s2)

    #first occurence of a word
    #if the word doesnt exist , it returns -1
    word = 'p'
    s4 = s.find(word)
    print(s4)

    #last occurence
    word = "to"
    s5 = s.rfind(word)
    print(s5)

    #count
    #count basically the ocuurence of the word
    word = 'a'
    s6 = s.count(word)
    print(s6)


    #are all the charcaters in the poem either letters or nums?
    print(s.isalnum())

    #case and alignment
    setup = 'a duck goes into a bar...'
    nodots = setup.strip('.')
    print(nodots)

    #capitalize
    print(setup.capitalize())
    print(setup.title())
    print(setup.upper())
    print(setup.lower())
    print(setup.swapcase())
    print(setup.center(30))
    print(setup.ljust(30))
    print(setup.rjust(30))

    s[2] = 'k'
    print(s)


def main():
    string_operations()

if __name__ == "__main__":
    main()
