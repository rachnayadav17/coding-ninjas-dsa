def triangle(x,y,z):
    if x == y == z:
        print("Equilateral Triangle")
    elif x == y or y == z or z == x:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
    
n=int(input())
n1=int(input())
n3=int(input())
triangle(n,n1,n3)