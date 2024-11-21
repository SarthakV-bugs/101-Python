# A. Create 3 lists X[5 Friends names], Y[5 Friends’ favorite dishes],Z[5 friends’ favorite
# restaurants]. Use zip to iterate through all these lists together and display:
#
# <X1 likes to eat Y1 at Z1>
#
# B. Create a 2D matrix [[1,2,3],[3,4,5],[5,6,7]]. Obtain the transpose of this matrix with
# zip - for two cases - with and without comprehension

#A.
X = ['Sharmishta',' Alan', 'Nandu', 'Sohel', 'Meenakshi' ]
Y = ['dosa', 'icecream', 'maggi', 'chicken', 'biscuit' ]
Z = ['dhabha', 'Naturals', 'hostel', 'curries and pickles', 'canteen' ]

for X, Y, Z in zip(X,Y,Z):
    print(f'{X} likes to eat {Y} at {Z}')



#B.
n = int(input("Enter the number: "))
# twoD_matrix = [[n,n+1,n+2]for n in range(1,n+1)]
twoD_matrix = [[n+1,n+2,n+3]for n in range(0,n+1)]
# #expression [n,n+1,n+2] gives list
# twoD_matrix = [['1','2','3']['3','4','5']]
twoD_matrix_t = []
for row in zip(*twoD_matrix):
    twoD_matrix_t.append(list(row))
print(twoD_matrix)
print(twoD_matrix_t)



