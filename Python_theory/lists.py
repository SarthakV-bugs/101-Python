def list_op():
  #   empty_list = []
  #   weekdays = ['monday', 'tuesday' , 'wed' , 'thurs' , 'fri' ,]
  #   another_empty_list = list()
  #   print(list('cat'))
  #   print(weekdays)
  #
  #
  # #tuple to list
  #
  #   a_tuple = ('ready' , 'fire' , 'aim')
  #   l = list(a_tuple)
  #   print(l)
  #
  #   #split #automatically creates a list
  #   birthday = '1/7/2001'
  #   blist = birthday.split('/')
  #   print(blist)
  #
  #   #access by index
  #   players = ['sarthak' , 'sharmistha' , 'srithi']
  #   print(players[0],players[1],players[2])
  #   print(players[-1],players[-2],players[-3])
  #
    #list of lists
    small_birds = ['hummingbird', 'finch']
    extinct_birds = ['dodo' , 'passenger pigeon' , 'Norwegian Blue']
    carol_birds = [3, 'french hens' , 2, 'turtledoves']
    all_birds = [small_birds, extinct_birds, 'macaw , carol_birds']
    print(all_birds)
    print(all_birds[0])
    print(all_birds[1][0])
  #
  #   #change an element of a list. lists are mutable
  #   players[1] = 'Rohit'
  #   print(players)
  #
  #
  #
  #   #use slices to get element
  #   # [start : end : step] extracts from the start offset to the end offset
  #   print(players[0:2])
  #   print(players[::2])
  #   print(players[::-2])
  #
  #
  #   #add to end by using append
  #   players.append("Rahul")
  #   print(players)


    # combine lists by using extend or +=
    players = ['sachin', 'Dhoni' , 'Virat' , 'Virat' , 'Rahul' , 'Virender']
    # bowlers = ['harbhajan' , 'bumrah']
    # all_players=players + bowlers
    # print(all_players)
    # players += bowlers
    # print(all_players)
    # players.extend(bowlers)
    # print(all_players)
    # players.extend(bowlers)
    # print(all_players)
    # players.append(bowlers)
    # print(all_players)



    #add an item by offset with insert
    # players.insert(3, "Shubham")

    #remove an item by offset and by value
    # del players[3]
    # players.remove("Rahul")
    # print(players)

    #pop
    # print(players.pop()) #pops the last element, like stacks
    # # print(players.pop(0)) #pops the first element
    #
    #
    # print(players.pop())
    # print(players.pop())


    #find an item's offset by value with index
    # print(players.index("Virat"))
    #
    # #test for a value using in
    # print("Dhoni" in players)
    #
    # #count occurrences of a value using count()
    # print(players.count("Virat"))

    #sort items in a list
    # players.sort() #inplace
    # print(players)
    # sortit = sorted(players)
    # # print(sortit)
    # players.sort(reverse=True)
    # print(players)
    # numbers = [2, 1, 4.0, 3]
    # print(numbers)
    # numbers.sort()
    # print(numbers)


    #get length using len
    # print(len(players))



    #assign with =, copy with copy()
    #assigning with = is a reference and not a copy

    # players_ref = players
    # print(players_ref)
    # players[0] = "Ishan"
    # print(players_ref)

    # players_copy = players.copy()
    # players_copy = list(players)
    # players_copy = players[:]
    # print(players_copy)
    # players[0] = "Virat"
    # print(players_copy)
    # print(players[:])






