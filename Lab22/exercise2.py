# Create a dictionary of friends with three keys { “name”, ” age ” , ” city ” }. Create a lambda
# function on a dictionary with the key age. Use this function with sorted() to sort the
# dictionary by age

friends = [{'name':'A','age':29,'City':'Mysore'},
           {'name':'B','age':23,'City':'Bengaluru'},
           {'name':'C','age':31,'City':'Mumbai'},
           ]
sorted_by_age = lambda x: x['age']
sorted_dict = sorted(friends, key=sorted_by_age)

print(sorted_dict)