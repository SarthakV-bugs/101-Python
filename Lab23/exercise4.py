# 4. A. Create a Function called CreateRepeats(n) that has an inner function repeat(string).
# This should repeat the string n times. The outer function CreateRepeats should return
# the inner function repeat . Create another function repeat_10 that calls
# CreateRepeats(10) and obtain repeat_10 as output function. Call repeat_10 with the
# string “Hello” as input . Observe the output.
# B. Repeat the above with CreateExponent(n) with the inner function exponent(m) that
# should return m**n. Create functions get_square, getCube by calling CreateExponent
# with 2, 3 as arguments. Call get_square, get_cube with different numbers and check the
# output.


def create_repeats(n):
    n1 = n
    def repeat(string):
        output = ([string*n1])
        return output
    return repeat

def create_exponent(n):
    def exponent(m):
        output = m**n
        return output
    return exponent




def main():
    repeat_10 = create_repeats(10)
    print(repeat_10('hello'))


 

if __name__ == "__main__":
    main()