def palindrom(n):
    res=0
    temp=n
    while n>0:
        r=n%10
        res=res*10+r
        n=n//10

    if temp==res:
        return True
    else:
        return False

    


n=int(input())
print(palindrom(n))

