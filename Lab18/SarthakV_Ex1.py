
# def gcd(n,m):
    # if n > m:
    #     return gcd(n-m, m)
    # elif m > n:
    #     return gcd(m-n, n)
    # else:
    #     return n
    
def gcd(n, m):
    d = min(n, m)
    while d > 0:
        if n % d == 0 and m % d == 0:
            return d
        d -= 1

# def lcm(n, m):
#     l = max(n, m)
#
#     while True:
#
#         if l % n == 0 and l % m == 0:
#             return l
#         l += 1




def main():
     n=int(input("Enter the number 1: "))
     m=int(input("Enter the number 2:"))

     # result=lcm(n,m)
     # print(f"The LCM of {n} and {m} is: {result}")
     #
     result=gcd(n,m)
     print(f"The greatest common divisor of 'n' and 'm' is {result}")



if __name__ == "__main__":
      main()