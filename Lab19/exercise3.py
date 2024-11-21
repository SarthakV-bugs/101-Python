# Create a list of tuples named friends_tuples
# (‘name’,’email-address’,age(INT)) of your friends. Create a dictionary
# friends_colleges with the above tuples as keys and values as their
# undergraduate college. Iterate over this dictionary and print the list of
# colleges.


friends_tuples = [('Alan', 'alan@gmail.com', 21),
                  ('Ronit', 'Ronit@gmail.com', 23),
                  ('Rohan', 'Rohan@gmail.com', 25)
                  ]

friends_colleges = {('Alan', 'alan@gmail.com', 21): "Kristu Jayanti",
                    ('Ronit', 'Ronit@gmail.com', 23): "MGM college",
                    ('Rohan', 'Rohan@gmail.com', 25) : "Harvard college"
                    }
for friends_tuples, colleges in friends_colleges.items():
    print(friends_colleges.values())





# friends_tuples = [('Alan', 'alan@gmail.com', 21),
#                   ('Ronit', 'Ronit@gmail.com', 23),
#                   ('Rohan', 'Rohan@gmail.com', 25)
#                   ]
# university=['Kristu Jayanti', 'MGM college', 'Harvard college']
#
# dict_frnds={}
# for i in range(len(friends_tuples)):
#     dict_frnds[friends_tuples[i]]=university[i]
#
# print(dict_frnds)
# print(dict_frnds.values())



