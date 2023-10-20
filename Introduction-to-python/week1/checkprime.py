def checkPrime(n):
    d=2
    flag=False
    while d<n:
        if n%d==0:
            flag=True
        d+=1
    
    if flag:
        print("not prime")
    else:
        print("prime")



n=int(input())
checkPrime(n)