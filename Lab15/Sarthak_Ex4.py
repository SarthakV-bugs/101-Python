#user.Display a message indicating the type of the triangle.

side1=int(input("Enter the side1: "))

side2=int(input("Enter the side2: "))

side3=int(input("Enter the side3: "))

if side1==side2==side3:
	print("It is a equilateral triangle")
elif side1==side2 or side2==side3 or side1==side3:
	print("It is an isoceles triangle")
else:
	print("It is a Scalene triangle")
