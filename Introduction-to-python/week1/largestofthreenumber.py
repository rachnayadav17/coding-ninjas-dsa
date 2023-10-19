def larger(n1,n2,n3):
    if n1>n2 and n1>n3:
        print("n1 is largest")
    elif n2>n3 and n2>n1:
        print("n2 is largest")
    else:
        print("n3 is largest")


n1=int(input())
n2=int(input())
n3=int(input())
larger(n1,n2,n3)
