def divisor(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
import math
def printDivisors(n) :  
    i = 1
    while i <= math.sqrt(n): 
        if (n % i == 0) :  
            if (n / i == i) : 
                print (i,end=" ") 
            else :  
                print (i , int(n/i), end=" ") 
        i = i + 1


n=int(input())
divisor(n)