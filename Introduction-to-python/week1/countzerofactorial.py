def countZero(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    res=0
    while fact%10==0:
        res+=1
        fact=fact//10
    return res

n=int(input())
print(countZero(n))