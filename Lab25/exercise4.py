def polygon():
    class Quadrilateral:
        def __init__(self, side1, side2, side3, side4):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
            self.side4 = side4

        def isSquare(self):
            if self.side1 == self.side2 == self.side3 == self.side4:
                return True
            return False

        def isRectangle(self):
            if self.side1 == self.side3 and self.side2 == self.side4:
                return True
            return False


    a1 = Quadrilateral(4, 4, 4, 4)
    print(a1.isSquare())
    print(a1.isRectangle())


    class Square(Quadrilateral):
        def __init__(self, side1):
            super().__init__(side1, side1, side1, side1)

        def getArea(self):
            return self.side1 * self.side1


    class Rectangle(Quadrilateral):
        def __init__(self, side1, side2):
            super().__init__(side1, side2, side1, side2)

        def getArea(self):
            return self.side1 * self.side2


    a2 = Square(5)
    print(a2.getArea())

    a3 = Rectangle(5, 6)
    print(a3.getArea())

def main():
    polygon()

if __name__ == "__main__":
    main()
