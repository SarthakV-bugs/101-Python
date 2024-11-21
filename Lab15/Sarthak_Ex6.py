#Write a program that reads a year from the user and displays the animal associated with that year.

year=int(input("Enter the year: "))


if year % 12 == 0:
    animal = "Dragon"
elif year % 12 == 1:
    animal = "Snake"
elif year % 12 == 2:
    animal = "Horse"
elif year % 12 == 3:
    animal = "Sheep"
elif year % 12 == 4:
    animal = "Monkey"
elif year % 12 == 5:
    animal = "Rooster"
elif year % 12 == 6:
    animal = "Dog"
elif year % 12 == 7:
    animal = "Pig"
elif year % 12 == 8:
    animal = "Rat"
elif year % 12 == 9:
    animal = "ox"
elif year % 12 == 10:
    animal = "Tiger"
elif year % 12 == 11:
    animal = "Hare"
else:
    animal = "Unknown"


print("The animal associated with the year", year, "is the", animal)


