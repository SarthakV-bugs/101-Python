#using list
def matrix_addition(a,b):
    c = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] + b[i][j]

    return c


def main():
    a = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    b = [[10,20,30],
         [40,50,60],
         [70,80,90]]
    matrix_addition(a,b)
    result=(matrix_addition(a,b))
    print(result)



if __name__ == "__main__":
     main()
