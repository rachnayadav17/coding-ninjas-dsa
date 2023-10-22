def isPrime(n):
    if n<=1:
        return False
    d=2
    flag=True
    while d<n:
        if n%d==0:
            flag=False
            break
        d+=1    
    return flag

def prime(n):
    for i in range(2,n+1):
        if isPrime(i):
            print(i)

def primeFactor(n):

    for i in range(2,n+1):
        if(isPrime(i)):
            x = n
            while x%i==0:
                print(i, end=" ")
                x = x//i

def maxPrimeFactor(n):
    mF = 1
    for i in range(2,n+1):
        if(isPrime(i) and n%i==0):
                mF = max(mF,i)
    print(mF)

def countPrimeFactor(n):
    count=0
    for i in range(2,n+1):
        if(isPrime(i)):
            x = n
            while x%i==0:
                count+=1
                x=x//i
    print(count)

n=int(input())
prime(n)