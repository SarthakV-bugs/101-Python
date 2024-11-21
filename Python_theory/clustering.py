
def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    low_list = []
    mid_list = []
    high_list = []

    for i in range(0, len(a)):
        if a[i] <= 10:
           low_list.append(a[i])
        elif (a[i] > 10) and (a[i] < 21):
            mid_list.append(a[i])
        else:
            high_list.append(a[i])


    print(low_list)
    print(mid_list)
    print(high_list)












if __name__ == "__main__":
    main()