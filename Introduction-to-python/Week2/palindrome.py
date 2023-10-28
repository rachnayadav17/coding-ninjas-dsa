def palindrome(n):
    reverse=0
    temp=n
    while n>0:
        r=n%10
        reverse=reverse*10+r
        n=n//10
    
    if temp==reverse:
        print("palindrome")
    else:
        print("not palindrome")



n=int(input())
palindrome(n)