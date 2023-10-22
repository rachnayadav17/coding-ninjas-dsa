def lcm(n,m):
    res=max(n,m)
    while True:
        if res%n==0 and res%m==0:
            return res
        res+=1

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return (a*b)//gcd(a,b)

n=int(input())
m=int(input())
print(lcm(n,m))