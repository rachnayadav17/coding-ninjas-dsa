def isPrime(n):
    d=2
    flag=False
    while d<n:
        if n%d==0:
            flag=True
            break
        d+=1
    
    if flag:
        print("Not goggly")
    else:
        print("goggly")
def digitSum(n):
    sum=0
    while n>0:
        r=n%10
        sum+=r
        n=n//10
    isPrime(sum)




n=int(input())
digitSum(n)