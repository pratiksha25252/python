import numpy as np
a=[]
n=int(input())
for i in range (n):
    v=int(input("a:"))
    a.append(v)
myarr=np.array(a)
print(myarr)
