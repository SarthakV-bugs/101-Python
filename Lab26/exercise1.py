
def multiply_matrix(A,B):
    if len(A[0]) is not len(B):  # A[0] is the first row of Matrix A
        return ValueError('Matrix dimensions not valid for Multiplication')


    out = [[0] * len(B[0]) for _ in range(len(A))]


    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)): #
                out[i][j] += A[i][k] * B[k][j]

             #matrix multiply general representation
    return out


def main():
    A = [[1,2],
         [3,4],
         [6,7]]

    B = [[1,2,3],
         [3,4,5]
         ]

    print(multiply_matrix(A,B))

    # print('Rows and columns for Matrix A and B')
    # rows_A = int(input('Enter the number of rows for Matrix A'))
    # columns_A = int(input('Enter the number of columns for Matrix A'))
    # rows_B = int(input('Enter the number of rows of Matrix B'))
    # columns_B = int(input('Enter the number of columns of Matrix B'))



if __name__ == '__main__':
    main()