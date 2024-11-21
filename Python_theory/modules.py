# modules vs packages

#module-any '.py file' is called a module, it might have multiple functions defined inside it
#linear algebra module can contain functions to compute eigenvectors,etc.
#import-used to reuse the module from open source

#packages-it is a folder which consists of multiple modules
#e.g. math pkg can consist of linearalgebra modules, calculus module, stats module
#import the pkg and then one can import the modules

import sys
# from and import to get one function from the module
#from and import as 'new func name' to import the function with a diff name
from collections import Counter, defaultdict, OrderedDict
import itertools
import sys #system related functions are present

# from Math2 import cal
# from Math2 import la
# from Math2 import stat
#
#
# cal.differentation()
# la.compute_lud()
# stat.median()

#setdefault() and defaultdict()

#setdefault
#defaultdict
#counter
#OrderedDict
#deque


# Collection pkg consists of deque, combining the benefits of stack and queues



def main():
    periodic_table = {'hydrogen': 1, 'Helium': 2}
    # print(periodic_table['nitrogen'])
    print(periodic_table.get('nitrogen'))
    print(periodic_table)
    print(periodic_table.setdefault('nitrogen',43))
    print(periodic_table)


    periodic_table=defaultdict(int)
    print(periodic_table['lithium'])    #0 will be th output

    lead_dict = defaultdict(lambda: 'Mydefaultvalue')
    lead_dict['hydrogen']=23
    print(lead_dict['helium'])  #mydefault value will be the output as helium isnt in the lead_dict
    print(lead_dict['hydrogen'])


    #
    # dict_counter = {}
    # for food in ['spam','spam','eggs','spam']:
    #     if food not in dict_counter



    breakfast = ['eggs','spam','eggs','bread','spam','spam']
    breakfast_counter = Counter(breakfast)
    print(breakfast_counter)

    print(breakfast_counter.most_common())
    print(breakfast_counter.most_common(2)) #the number 1,2.etc basically is the number of items you want to pull

    #counter obj can be used with an arithmetic operator
    lunch = ['eggs', 'bacon', 'eggs']
    lunch_counter = Counter(lunch)
    print(breakfast_counter + lunch_counter)
    print(breakfast_counter - lunch_counter)
    print(breakfast_counter & lunch_counter)
    print(breakfast_counter | lunch_counter)


    #order by key with OrderDict()

    #order of keys in a dictionary is not predictable
    scores = {'Shubham': 100,'Virat':0, 'Rohit':200}
    for score in scores:
        print(score)



    scores = OrderedDict([('Shubham',100),('Rohit',200),('Virat',0)])
    for score in scores:
        print(score)

    def palindrome(word):
        from collections import deque
        dq = deque(word)
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
            return True
    #
    # print(palindrome(racecar))



if __name__ == "__main__":
        main()