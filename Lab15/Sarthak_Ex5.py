##Write a program that begins by reading the number of loaves of day old bread being purchased from the user.


number=int(input("Enter the number of loaves purchased: "))

Regular_price=25.50
discounted_price=0.6*25.50
Total_Regular_price=Regular_price*number
Total_discounted_price=number*discounted_price
Total=Total_Regular_price-Total_discounted_price

print("The total price is %5.2f" %Total)
