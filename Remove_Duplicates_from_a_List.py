a=[1,2,2,3,1]
m=[]
b=a.count(1)
c=a.count(2)
d=a.count(3)
if b>1:
     a.remove(1)
m.append(1)
if c>1:
       a.remove(2)
m.append(2)
if d>1:
    a.remove(3)
m.append(3)

print(a,m)

        

