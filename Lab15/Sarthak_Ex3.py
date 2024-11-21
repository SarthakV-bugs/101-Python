#Create a program that reads the name of a month from the user as a string. 

#Input
month=str(input("Enter Month: "))

days=31
if 	month=="April" or month=="June"\
	or month=="September" or month=="November":
		days=30
elif month=="February":
		days="28 or 29"

print("The month of", month, "has", days, "days")


