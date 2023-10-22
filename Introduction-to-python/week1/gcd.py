def gcd(n,m):
    k = min(n,m)
    ans = 1
    for i in range(2,k+1):
        if n%i==0 and m%i==0:
            ans = i
    return ans


n=int(input())
m = int(input())
print(gcd(n,m))

