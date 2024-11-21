from math import sqrt
def main():
    perimeter=0
    first_x = input("Enter the value of x coordinate or blank to quit: ")
    if first_x == "":  # Use comparison instead of assignment
        exit()  # Exit if input is blank
    first_x = float(first_x)
    first_y =float(input("Enter the value of y coordinate: "))
    last_x=first_x
    last_y=first_y
    while True:
        line1 = input("Enter the value of x coordinate or blank to quit: ")
        if line1 == "":  # Break if input is blank
            break
        x = float(line1)
        y = float(input("Enter the value of y coordinate: "))
        dist=sqrt((x-first_x)**2+(y-first_y)**2)
        perimeter+=dist
        last_x = x
        last_y = y
    dist = sqrt((last_x - first_x) ** 2 + (last_y - first_y) ** 2)
    perimeter+=dist
    print(f"The perimeter of the polygon is {perimeter}")
if __name__=="__main__":
    main()

