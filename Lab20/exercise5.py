import random

def bubble_sort(a):
    l=len(a)
    for i in range(0,l):
        for j in range(l-1,i,-1):
            if a[j-1] > a[j]:
                a[j],a[j-1]=a[j-1],a[j]
    return a

def main():
    a = [ random.randint(0,100) for _ in range(1,100) ]
    print(a)
    print(bubble_sort(a))

if __name__ == '__main__':
    main()