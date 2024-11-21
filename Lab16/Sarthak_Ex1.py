def decimal_to_binary(n):

    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def main():
    decimal_num = int(input("Enter the decimal number: "))
    binary_num = decimal_to_binary(decimal_num)
    print(binary_num)




if __name__ == "__main__":
        main()