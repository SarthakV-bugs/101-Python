#How OOP can be implemented in python?
#structured programming - C programming
# object-oriented programming
# why was it proposed?
#what is an object?
#attributes(properties) and variables
#
# """difference between class and object - Furniture = class, sofa = object """
# """ object is an instantiation of class, a lot of object can be created using a class """
# """class can have as many attributes and method"""
# class Person: #class and class name
#     #what is self doing? reference to the obj which you have created
#     def __init__(self,myname,mycity): #takes two parameter, multiple args can be passed
#         """property/attribute declaration of class"""
#         self.name = myname #property defined within the class person, here its '.name'
#         self.city = mycity
#
#
#     #method declaration
#     def person_score_avg(self):
#
#
#
#      #constructors??? initialize the property of object during object creation
#     #class instantiation
# #     #Object creation
#
#
# player=Person('Sarthak','mumbai')
# print(player.city)
# print(player.name)


"""
    Inheritance-derived class/subclass/child
    Parent class(superclass/base class) > child(child class/derived class/subclass)"""
#
# class Player:
#     def display(self):
#         print('This is a player')
#
# class Cricket_Player(Player):
#     def display(self):
#         print('The person is a cricket player')
#
#     def matches(self):
#         print('The person has played 100 matches')
#
# # Create an instance of Player
# p = Player()
# p.display()  # Output: This is a player
#
# # Create an instance of Cricket_Player
# c = Cricket_Player()
# c.display()  # Output: The person is a cricket player
# c.matches()  # Output: The person has played 100 matches
#
#
#

#inheritance- reuse a functionality, polymorphism,data encapsulation
#class method-A class method in Python is a method that is bound to the class and not the instance of the class.
# static method-


#polymorphismIn
# Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class.
# class Player:
#     def who(self):
#         return self.person
#
#     def says(self):
#         return self.words + '.'
#
# class Batsman(Player):
#     def says(self):
#         return self.words + 'batsman'
#
# class Bowler(Player):
#     def says(self):
#         return self.words + 'bowler'
#
# p = Player('sachin', "I'm a player")
# print(p.who(), 'says:', p.says())
# p1 = Batsman('rohith','im a ' )
# print(p1.who(),'says:',p1.says())

##magic methods

class Word():
    def __init__(self,text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('Ha')
third = Word('eh')
print(first == second )
print(first == third)
print(first)
print(first.__eq__(second))






