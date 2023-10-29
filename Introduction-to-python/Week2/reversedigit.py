def reverseDigit(n):
    reverse=0
    while n>0:
        r=n%10
        reverse=reverse*10+r
        n=n//10
    return reverse


n=int(input())
print(reverseDigit(n))