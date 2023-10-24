def sum(n):
    # sum=0
    # for i in range(1,n+1):
    #     sum+=i
    # print(sum)

    sum=0
    i=1
    while i<=n:
        sum+=i
        i=i+1
    print(sum)

n=int(input())
sum(n)