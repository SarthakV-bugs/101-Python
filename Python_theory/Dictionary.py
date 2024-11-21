def dictops():

    # empty_dict = {}
    # scores = {"Rahul": 99, "Shubham": 100, "Virat": 120, "Dhoni": 0}
    # print(scores)
    # print(scores["Shubham"])
    #
    #
    # #convert using two value sequences
    # # a will be key, b will be value
    # lol = [ ['a','b'], ['c','d'], ['e','f']]
    # print(dict(lol))
    #
    #
    # #list of two items tuple
    # lot = [('a','b'), ('c','d'), ('e','f')]
    # print(dict(lot))
    #
    # #tuple of two item lists
    tol = (['a','b'], ['c','d'], ['e','f'])
    print(dict(tol))


    #combine dict with updates\


    # dictplayers = {
    #     "Rohit": 78,
    #     "Gill": 80,
    #     "Kohli": 45,
    # }
    #
    # dictnew = {
    #     "bumrah": 30,
    #     "siraj": 20
    # }
    #
    # dictplayers.update(dictnew)
    # print(dictplayers)
    # print(dictnew)
    #
    #
    # #delete an item key with del
    # del dictplayers["siraj"]








#     # test for a key by using in
#     "Rohit" in dictplayers
#
#     # get an item by [key]
#
#     print(dictplayers["Gill"]) #only value retrieve method 1
#     # print(dictplayers["shyam"]) #throws key error as shyam not a key
#     # print(dictplayers.get("Gill")) #only value retrieve method 2
#     print(dictplayers.get("Shyam", 'Not Present')) #userfriendly msg like 'not present'  if key shyam is not there
# #
# #
#     #get all keys
#     dictplayers.keys()
#     print(list(dictplayers.keys()))
#
#     #get all values
#     print(list(dictplayers.values()))
#
#
#     #get all key value pairs using items
#
#     print(list(dictplayers.items()))
#
# new_dict = {
#         "bumrah": 30,
#         "siraj": 20,
#          130: "some"
# # }
# print(new_dict)

def main():
    dictops()

if __name__ == "__main__":
        main()