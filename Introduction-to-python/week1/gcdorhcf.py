def hcf(n,m):
    res=min(n,m)
    while res>0:
        if n%res==0 and m%res==0:
            break
        res-=1
    return res

def hcf(n,m):
    while n!=m:
        if n>m:
            n= n-m
        else:
            m= m-n
    return n

def hcf(n,m):
    if m==0:
        return n
    return hcf(m,n%m)


n=int(input())
m=int(input())
print(hcf(n,m))