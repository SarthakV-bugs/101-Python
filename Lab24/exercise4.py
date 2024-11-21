x=10
def checkNameSpaces():
    z=2
    global x
    x = 4
    print(x)
    print(z)
    print(globals())
    print(locals())
    
checkNameSpaces()