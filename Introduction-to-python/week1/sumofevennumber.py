def sumEven(n):
    sum=0
    for i in range(1,n+1):
        if i%2==0:
            sum+=i
    print(sum)

n=int(input())
sumEven(n)