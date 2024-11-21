from Utils import math_utils
from Utils.math_utils import add
from Utils import math_utils as mu
from Utils import String_utils
from Utils.String_utils import concatenate
from Utils import String_utils as su
def mathutil():
    math_utils.add(3,4)
    math_utils.sub(4,3)
    math_utils.mult(5,6)
    math_utils.rem(9,6)
    math_utils.quot(6,2)
    add(3,4)


    mu.mult(10,2)
    mu.rem(7,5)

    String_utils.str_lower("Sarthak")
    String_utils.str_upper("sarthak")
    String_utils.concatenate("Hello","Bye")
    concatenate("Hi","welcome")
    su.str_upper("biology")
    su.concatenate("hello","world")

def main():
    mathutil()

if __name__=="__main__":
    main()