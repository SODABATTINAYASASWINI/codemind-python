n=input()
l=list(n)
v=[]
k=[]
for i in l:
   v.append(int(i))
o=1
for j in v:
   p=j**o
   k.append(p)
   o+=1
c=sum(k)
y=str(c)
if(y==n):
   print(True)
else:
   print(False)