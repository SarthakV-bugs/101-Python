# Create a nested dictionary where the keys are numbers from 1 to N, and the values
# are dictionaries where the keys are "square" and "cube" with their respective values.
# Take N as an input from the user.
# {1:{“square”:1, “cube”,1},2:{“square”:4,”cube”:8}.......}
#Create a tuple of tuples such as ((1,1,1),(2,4,8)...)using comprehension
# Create an identity matrix of dimension N using comprehension. Print the identity
# matrix row-wise.



def main():
    n = int(input("Enter the number: "))
    dict1 = {n:{"square":n**2, "cube":n**3} for n in range(1,n+1)}
    print(dict1)

    tuple1= tuple((n,n**2,n**3)for n in range(1,n+1))
    print(tuple1)

    # #identity matrix
    identity_matrix = [[1 if i==j else 0 for j in range(1,n+1)] for i in range(1,n+1)]
    for rows in identity_matrix:
        print(rows)

    # empty_matrix=[[0 for _ in range(n)]for _ in range(n)]
    # print(empty_matrix)
    # for i in range(n):
    #     for j in range(1,n+1):
    #         if i==j:
    #             empty_matrix[i][j] = 1
    # print(empty_matrix)


    #english_spanish dictionary
    English=  ['run', 'eat', 'sleep', 'write', 'speak']
    Spanish= ['correr', 'comer', 'dormir', 'escribir', 'hablar']

    eng_spn_dict = dict(zip(English, Spanish))
    print(eng_spn_dict)



if __name__ == "__main__":
        main()