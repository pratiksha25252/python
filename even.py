import math
a=int(input("a"))
b=int(input("b:"))
c=int(input("c:"))

d=b**2-4*a*c
if(d>0):
    r=(-b+math.sqrt(d))/2*a
    s=(-b-math.sqrt(d))/2*a
    print(r)
    print(s)
    print("real and distinct")
elif(d==0):
    r=-b/2*a
    s=-b/2*a
    print(r)
    print(s)
else:
    print("roots are imaginary")

    
