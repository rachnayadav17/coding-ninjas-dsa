def sumEvenOdd(n):
    evensum=0
    oddsum=0

    while n>0:
        r=n%10
        if r%2==0:
            evensum=evensum+r
        else:
            oddsum=oddsum+r
        n=n//10
    print(evensum,oddsum)



n=int(input())
sumEvenOdd(n)