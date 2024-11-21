from SarthakV_Ex1 import gcd

def fraction(numerator,denominator):
    d = gcd(numerator,denominator)
    new_n = numerator // d
    new_d = denominator // d
    return new_n,new_d


def main():
    numerator=int(input('Enter the numerator of the fraction:'))
    denominator=int(input('Enter the denominator of the number:'))

    new_n, new_d = fraction(numerator, denominator)

    print(f"The reduced fraction is {new_n}/{new_d}" )
    



if __name__ == "__main__":
      main()