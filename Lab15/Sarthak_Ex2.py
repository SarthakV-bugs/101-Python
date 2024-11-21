#Write a program that determines the name of a shape from its number of sides.
#write it with name=""

#Input prompt
sides=int(input("Enter the number of sides: "))

#error check
if sides<3 or sides>10:
	print("Error: Input not within range")

#Condition block
if sides== 3:
	print("It's a Triangle")
elif sides==4:
	print("It's a Quadrilateral")
elif sides==5:
	print("It's a Pentagon")
elif sides==6:
	print("It's a Hexagon")
elif sides==7:
	print("It's a heptagon")
elif sides==8:
	print("It's a Octagon")
elif sides==9:
	print("It's a Nonagon")
elif sides==10:
	print("It's a Decagon")
