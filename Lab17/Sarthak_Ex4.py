#Christmas song
# from Lab17.Sarthak_Ex3 import get_ordinal_number
#
#
# def verse():
#     n= int(input("Enter the verse day: "))
#     print(f"On the {get_ordinal_number(n)} day of Christmas, i got")
#
#     if n >= 5:
#         print("Five Golden Rings,")
#     if n >= 4:
#         print("Four calling birds,")
#     if n >= 3:
#         print("Three French Hens,")
#     if n >= 2:
#         print("Two turtle doves")
#
#     if n == 1:
#         print("A partridge in a pear tree.")
#     else:
#         print("And a partridge in a pear tree.")
#     print()

#### implementation using dictionary

def get_ordinal(n):
    ord_dict = {1:"first", 2:"second", 3:"third", 4:"fourth", 5:"fifth"}
    return ord_dict[n]    #to retrieve the value

def get_gift(n):
    gift_day = {1:"A partridge in a pear tree.",
                2: "Two turtle doves",
                3: "Three French Hens,",
                4: "Four calling birds,",
                5: "Five Golden Rings,"
        }
    return gift_day[n]

def verse(n):
    for n in range(1,n+1):
        j = n
        print(f"On the {get_ordinal(j)} day of Christmas, i got")


        while j > 0:
            if n>1 and j==1:
                print("And a")
            print(f"{get_gift(j)}")
            j = j-1




def main():
    n = int(input("Enter the number:"))
    verse(n)
    # day = get_ordinal(n)
    # print(day)
    #
    # gift = get_gift(n)
    # print(gift)


if __name__ == "__main__":
    main()
