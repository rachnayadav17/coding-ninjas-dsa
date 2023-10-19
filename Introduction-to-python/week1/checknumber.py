def checkNumber(n):
    if n>0:
        print("{} is positive".format(n))
    elif n<0:
        print("n is negative")
    else:
        print("n is neigther positive nor negative")


n=int(input())
checkNumber(n)